import logging
import re
import string
import collections
import nltk
from typing import Any, Callable, Dict, Generator, Sequence

logger = logging.getLogger(__name__)

def chunks(l: Sequence, n: int = 5) -> Generator[Sequence, None, None]:
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def stride_chunks(l: Sequence, win_len: int, stride_len: int):
    s_id = 0
    e_id = min(len(l), win_len)

    while True:
        yield s_id, l[s_id:e_id]

        if e_id == len(l):
            break

        s_id = s_id + stride_len
        e_id = min(s_id + win_len, len(l))


def convert_examples_to_features(tokenizer, data, max_input_length, merge_pred=False, stride=0):
    features = []
    for example_idx, d in enumerate(data):
        doc = _normalize_text(d['doc'])
        q = _normalize_text(d['q'])
        if not merge_pred:
            temp = tokenizer.encode_plus(q, doc, return_offsets_mapping=True, truncation=False)
            # cut by max_input_length
            input_ids = temp.data['input_ids']
            if len(input_ids) > max_input_length:
                logger.info("Input length {} is too big. Cap to {}".format(len(input_ids), max_input_length))
                for k, v in temp.data.items():
                    temp.data[k] = cap_to(v, max_input_length)

            temp['doc'] = doc
            temp['q'] = q
            temp['example_idx'] = example_idx
            features.append(temp)
        else:   # tokenize, split by stride, then encode
            seq_pair_added_toks = tokenizer.model_max_length - tokenizer.max_len_sentences_pair
            q_toks = tokenizer.tokenize(q)
            window_len = max_input_length - len(q_toks) - seq_pair_added_toks
            doc_enc = tokenizer.encode_plus(doc, add_special_tokens=False, return_offsets_mapping=True, truncation=False)
            for base_idx, chunk_mapping in stride_chunks(doc_enc['offset_mapping'], window_len, stride):
                chunk_st = chunk_mapping[0][0]
                chunk_ed = chunk_mapping[-1][0]
                chunk = doc[chunk_st: chunk_ed]
                temp = tokenizer.encode_plus(q, chunk, return_offsets_mapping=True, truncation=False)
                temp['doc'] = chunk
                temp['orig_doc'] = doc
                temp['q'] = q
                temp['example_idx'] = example_idx
                temp['base_idx'] = base_idx
                temp['orig_offset_mapping'] = doc_enc['offset_mapping']
                features.append(temp)

    return features

def merge_predictions(results):
    idx_res_map = collections.OrderedDict()
    for r in results:
        example_idx = r.get('example_idx')
        if example_idx not in idx_res_map:
            idx_res_map[example_idx] = r
        else:
            if r['prob'] > idx_res_map[example_idx]['prob'] and not r.get('missing_warning'):
                idx_res_map[example_idx] = r

    results = [v for v in idx_res_map.values()]
    return results

    

def pad_batch(batch):
    max_len = max([len(f['input_ids']) for f in batch])
    for f in batch:
        f_len = len(f['input_ids'])
        f['length'] = f_len
        f['input_ids'] = f['input_ids'] + [0] * (max_len - f_len)
        f['token_type_ids'] = f['token_type_ids'] + [0] * (max_len - f_len)
        f['attention_mask'] = f['attention_mask'] + [0] * (max_len - f_len)

    input_ids = [f['input_ids'] for f in batch]
    token_type_ids = [f['token_type_ids'] for f in batch]
    attn_masks = [f['attention_mask'] for f in batch]

    return input_ids, token_type_ids, attn_masks
        

def _normalize_text(text):
    return re.sub('\s+', ' ', text)

def cap_to(seq, max_len):
    prefix = seq[0:-1][0:max_len - 1]
    return prefix + [seq[-1]]

def get_span_from_ohe(bio_labels):
    left = 0
    right = 1
    found_st = False
    found_ed = False
    span_indexes = []

    while right < len(bio_labels):
        if not found_st and not found_ed:
            if bio_labels[right] == 0:
                right += 1
                continue
            else:
                found_st = True
                left = right
        if found_st:
            if bio_labels[right] == 1:
                right += 1
                continue
            else:
                span_indexes.append((left, right-1))
                left = right
                right = left + 1
                found_st = False
                found_ed = False

    if set(bio_labels[left:right]) == {1}:
        span_indexes.append((left, right-1))
    
    return span_indexes

def get_ans_span(res):
    if not res:
        return ""

    for i, t in enumerate(res):
        if t.startswith("##"):
            res[i - 1] += t[2:]
            res[i] = ""

    value = " ".join([x for x in res if x != ""])
    return value

def is_whitespace(c):
    if c == " " or c == "\t" or c == "\r" or c == "\n" or ord(c) == 0x202F:
        return True
    return False

def token2char(orig_str, tokens):
    norm_tokens = [t.replace('##', '') for t in tokens]

    token_id = 0
    token_char_id = 0
    token2char_map = {}  # token_id -> [start, end]

    token2char_map[token_id] = [0, None]
    for c_id, c in enumerate(orig_str):
        if is_whitespace(c):
            token2char_map[token_id][1] = c_id
            token_id += 1
            token_char_id = 0
            token2char_map[token_id] = [c_id+1, None]
            continue

        if token_char_id < len(norm_tokens[token_id]) and c == norm_tokens[token_id][token_char_id]:
            token_char_id += 1
        else:
            token2char_map[token_id][1] = c_id
            token_id += 1
            token_char_id = 0
            token2char_map[token_id] = [c_id, None]

            if c == norm_tokens[token_id][token_char_id]:
                token_char_id += 1

    token2char_map[token_id][1] = c_id+1
    # print(token2char_map)
    return token2char_map



class EnAnswerComparator(object):

    def get_tokens(self, s):
        if not s: return []
        return self.normalize_answer(s).split()

    @classmethod
    def normalize_answer(cls, s):
        """Lower text and remove punctuation, articles and extra whitespace."""

        def remove_articles(text):
            regex = re.compile(r'\b(a|an|the)\b', re.UNICODE)
            return re.sub(regex, ' ', text)

        def white_space_fix(text):
            return ' '.join(text.split())

        def remove_punc(text):
            exclude = set(string.punctuation)
            return ''.join(ch for ch in text if ch not in exclude)

        def lower(text):
            return text.lower()

        return white_space_fix(remove_articles(remove_punc(lower(s))))

    def compute_em(self, a_gold, a_pred):
        return int(self.normalize_answer(a_gold) == self.normalize_answer(a_pred))

    def compute_f1(self, a_gold, a_pred):
        gold_toks = self.get_tokens(a_gold)
        pred_toks = self.get_tokens(a_pred)
        common = collections.Counter(gold_toks) & collections.Counter(pred_toks)
        num_same = sum(common.values())
        if len(gold_toks) == 0 or len(pred_toks) == 0:
            # If either is no-answer, then F1 is 1 if they agree, 0 otherwise
            return int(gold_toks == pred_toks)
        if num_same == 0:
            return 0
        precision = 1.0 * num_same / len(pred_toks)
        recall = 1.0 * num_same / len(gold_toks)
        f1 = (2 * precision * recall) / (precision + recall)
        return f1


class ZhAnswerComparator(object):

    # split Chinese with English
    def mixed_segmentation(self, in_str, rm_punc=False):
        in_str = str(in_str).lower().strip()
        segs_out = []
        temp_str = ""
        sp_char = ['-', ':', '_', '*', '^', '/', '\\', '~', '`', '+', '=',
                   '，', '。', '：', '？', '！', '“', '”', '；', '’', '《', '》', '……', '·', '、',
                   '「', '」', '（', '）', '－', '～', '『', '』']
        for char in in_str:
            if rm_punc and char in sp_char:
                continue
            if re.search(r'[\u4e00-\u9fa5]', char) or char in sp_char:
                if temp_str != "":
                    ss = nltk.word_tokenize(temp_str)
                    segs_out.extend(ss)
                    temp_str = ""
                segs_out.append(char)
            else:
                temp_str += char

        # handling last part
        if temp_str != "":
            ss = nltk.word_tokenize(temp_str)
            segs_out.extend(ss)

        return segs_out

    # remove punctuation
    def remove_punctuation(self, in_str):
        in_str = str(in_str).lower().strip()
        sp_char = ['-', ':', '_', '*', '^', '/', '\\', '~', '`', '+', '=',
                   '，', '。', '：', '？', '！', '“', '”', '；', '’', '《', '》', '……', '·', '、',
                   '「', '」', '（', '）', '－', '～', '『', '』']
        out_segs = []
        for char in in_str:
            if char in sp_char:
                continue
            else:
                out_segs.append(char)
        return ''.join(out_segs).strip()

    # find longest common string
    def find_lcs(self, s1, s2):
        m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        mmax = 0
        p = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    m[i + 1][j + 1] = m[i][j] + 1
                    if m[i + 1][j + 1] > mmax:
                        mmax = m[i + 1][j + 1]
                        p = i + 1
        return s1[p - mmax:p], mmax

    def compute_em(self, a_gold, a_pred):
        return int(self.remove_punctuation(a_gold) == self.remove_punctuation(a_pred))

    def compute_f1(self, a_gold, a_pred):
        ans_segs = self.mixed_segmentation(a_gold, rm_punc=True)
        prediction_segs = self.mixed_segmentation(a_pred, rm_punc=True)
        lcs, lcs_len = self.find_lcs(ans_segs, prediction_segs)
        if lcs_len == 0:
            f1 = 0.0
        else:
            precision = 1.0 * lcs_len / len(prediction_segs)
            recall = 1.0 * lcs_len / len(ans_segs)
            f1 = (2 * precision * recall) / (precision + recall)
        return f1
from scapy.utils import chexdump

from scapy_helper.helpers.depracated import deprecated


def _diff(first, second):
    first = _prepare(first)
    second = _prepare(second)

    _fill_empty_elements(first, second)

    first_row = []
    second_row = []
    diff_indexes = []
    for e, _ in enumerate(first):
        if first[e].lower() != second[e].lower():
            first_row.append(first[e])
            second_row.append(second[e])
            diff_indexes.append(e)
            continue
        first_row.append("__")
        second_row.append("__")
    return first_row, second_row, diff_indexes


def _fill_empty_elements(first, second):
    if len(first) != len(second):
        print("WARN:: Frame len is not the same")

        len_first = len(first)
        len_second = len(second)
        if len_first > len_second:
            print("WARN:: First row is longer by the %sB\n" % (len_first - len_second))
            for x in range(len_first - len_second):
                second.append("  ")
        else:
            print("WARN:: Second row is longer by the %sB\n" % (len_second - len_first))
            for x in range(len_second - len_first):
                first.append("  ")


def _prepare(obj):
    if not isinstance(obj, str):
        obj = get_hex(obj)
    if isinstance(obj, str):
        obj = obj.split()
    return obj


def get_hex(frame):
    return ' '.join([x.replace("0x", "").replace(",", "") for x in chexdump(frame, dump=True).split()])


def show_hex(frame):
    print(get_hex(frame))


def _create_diff_indexes_list(indexes):
    new_list = []
    for x in range(max(indexes) + 1):
        new_list.append("  ")
    for idx in indexes:
        if idx < 10:
            new_list[idx] = str("^%s" % idx)
        else:
            new_list[idx] = str(idx)
    new_list.append("| position")
    return ' '.join(new_list)


def show_diff(first, second, index=False, extend=False, empty_char="XX"):
    first_row, second_row, indexes_of_diff = _diff(first, second)
    first_row_len_bytes = count_bytes(first_row)
    second_row_len_bytes = count_bytes(second_row)

    for row in (first_row, second_row):
        for idx, element in enumerate(row):
            if element == "  ":
                row[idx] = empty_char

    print(' '.join(first_row), "| len: %sB" % first_row_len_bytes)
    print(' '.join(second_row), "| len: %sB" % second_row_len_bytes)
    if index and indexes_of_diff:
        str_bar = "   " * first_row_len_bytes if first_row_len_bytes > second_row_len_bytes else \
            "   " * second_row_len_bytes
        print("%s|\n%s" % (str_bar, _create_diff_indexes_list(indexes_of_diff)))

    if extend:
        more_info = []
        for types in first.class_fieldtype.items():
            for el in types[1].items():
                more_info.append((el[0], el[1].sz))
        print(more_info)

    print()
    if indexes_of_diff:
        print("Not equal at {}B".format(len([x for x in first_row if x != "__"])))
        return True
    elif len([x for x in first_row if x != "__"]) == len(first_row):
        print("Not equal")
        return True
    print("Ok")
    return False


def count_bytes(packet_hex_list):
    return len([x for x in packet_hex_list if x != "  "])


def get_diff(*args):
    raise NotImplementedError


def get_diff_status(first, second):
    _, _, status = _diff(first, second)
    return status


@deprecated
def table(first, second):
    f, s, status = _diff(first, second)
    show_diff(first, second)
    f_details = first.show(dump=True).split("\n")
    s_details = second.show(dump=True).split("\n")

    for r in range(len(f_details)):
        print("{} {:>40}".format(f_details[r], s_details[r]))

    return status

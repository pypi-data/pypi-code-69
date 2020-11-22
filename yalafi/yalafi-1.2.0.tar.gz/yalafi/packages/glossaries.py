
#
#   YaLafi module for LaTeX package glossaries
#
#   Conditions for operation
#   ------------------------
#   - We rely on the .glsdefs database file generated by package glossaries.
#     Note that the .glsdefs file is only generated, if the definitions with
#     \newacronym, \newglossaryentry etc. are not placed in the LaTeX preamble,
#     but inside of \begin{document} ... \end{document}. Be aware that you
#     might need to call twice (latex + makeglossaries + latex) in order to
#     obtain a completely updated .glsdefs file.
#   - All LaTeX files have to read this database, before \gls etc. can be
#     expanded by the filter. This may be done with
#       \newcommand{\LTinput}[1]{}  % only, if not yet seen by LaTeX
#                                   % --> better placed in document preamble
#       \LTinput{main.glsdefs}
#     Here, the LaTeX file 'main.tex' invokes \makeglossaries in the preamble.
#   - Please note that the path to main.glsdefs has to be valid at the moment
#     YaLafi is called, e.g., when starting a proofreader via an editor plugin.
#     If you invoke the editor at a subdirectory of the LaTeX project, then you
#     might have to write something like \LTinput{../main.glsdefs}.
#     A good way is to use something like `vi ch-Banach/open-mapping.tex`.
#   - Call of \LTinput{file.glsdefs} also can be done in an auxiliary
#     file that contains custom YaLafi macro definitions, say custom.tex.
#     This file in turn may be included by \LTinput{custom.tex} into each
#     LaTeX source. Alternatively, it may be passed by option --defs
#     or --define to yalafi or yalafi.shell, respectively. (In this case,
#     which does not require a change of the LaTeX source, custom.tex should
#     contain \usepackage{glossaries} before \LTinput{file.glsdefs}, or
#     the package name should be passed with options --pack / --packages.)
#
#   Behaviour of macros
#   -------------------
#   - \newacronym and \newglossaryentry create plain-text output from the
#     description. We start with a capital letter, and append a dot. The
#     latter is only done, if the text does not end in one of '.!?'.
#   - For the simple \gls commands, we always use the 'text' entry, as this
#     is available for all glossary entries in .glsdefs. The same accounts for
#     all plural forms, where we use entry 'plural'.
#   - We have not yet implemented the trailing optional argument of \gls etc.
#     Currently, this would consume subsequent space, if this argument is
#     missing; compare the behaviour of \footnotemark[] and
#     \newtheorem{}[]{}[].
#

import copy
from yalafi import defs, utils
from yalafi.defs import Macro, InitModule

require_packages = []

def init_module(parser, options):
    parms = parser.parms

    macros_latex = ''

    macros_python = [

        Macro(parms, '\\gls', args='OA', repl=h_gls('text', [])),
        Macro(parms, '\\glspl', args='OA', repl=h_gls('plural', [])),
        Macro(parms, '\\Gls', args='OA', repl=h_gls('text', [cap_first])),
        Macro(parms, '\\Glspl', args='OA', repl=h_gls('plural', [cap_first])),
        Macro(parms, '\\GLS', args='OA', repl=h_gls('text', [cap_all])),
        Macro(parms, '\\GLSpl', args='OA', repl=h_gls('plural', [cap_all])),

        Macro(parms, '\\glsdesc', args='OA',
                                    repl=h_gls('description', [])),
        Macro(parms, '\\Glsdesc', args='OA',
                                    repl=h_gls('description', [cap_first])),
        Macro(parms, '\\GLSdesc', args='OA',
                                    repl=h_gls('description', [cap_all])),

        Macro(parms, '\\glsdisp', args='OAA', repl='#3'),
        Macro(parms, '\\glslink', args='OAA', repl='#3'),

        Macro(parms, '\\glstext', args='OA', repl=h_gls('text', [])),
        Macro(parms, '\\Glstext', args='OA', repl=h_gls('text', [cap_first])),
        Macro(parms, '\\GLStext', args='OA', repl=h_gls('text', [cap_all])),

        Macro(parms, '\\longnewglossaryentry', args='AAA', repl=h_newacronym),
        Macro(parms, '\\newacronym', args='AAA', repl=h_newacronym),
        Macro(parms, '\\newglossaryentry', args='AA', repl=h_newglossaryentry),

        # this is for reading the .glsdefs database
        Macro(parms, '\\gls@defglossaryentry', args='AA',
                                                    repl=h_parse_glsdefs),

    ]

    environments = []

    return InitModule(macros_latex=macros_latex, macros_python=macros_python,
                        environments=environments)

#   return a handler function:
#   - read glossary entry with label given in macro argument
#   - get token list for specified key
#   - apply list of modifications
#   - set all token positions to beginning of \gls macro
#
def h_gls(key, mods):
    def f(parser, buf, mac, args, pos):
        toks = get_tokens(parser, args[1], key)
        if toks is None:
            return utils.latex_error('could not find label for \\gls...'
                    + ' - did you include "\\LTinput{<main file>.glsdefs}"?',
                    pos, parser.latex, parser.parms)
        for f in mods:
            toks = f(toks)
        for t in toks:
            t.pos = pos
            t.pos_fix = True
        return toks
    return f

def h_newacronym(parser, buf, mac, args, pos):
    return modify_description(parser, args[2])

def h_newglossaryentry(parser, buf, mac, args, pos):
    descr = parser.parse_keyvals_dict(args[1]).get('description', [])
    return modify_description(parser, descr)

the_glossary = {}

#   main task: parse 'key={...},key={...},...' in second macro argument
#
def h_parse_glsdefs(parser, buf, mac, args, pos):
    label = parser.get_text_expanded(args[0])
    the_glossary[label] = parser.parse_keyvals_dict(args[1])
    return []

#   get token list for a key, database label given as token list
#
def get_tokens(parser, label, key):
    label = parser.get_text_expanded(label)
    if label not in the_glossary or key not in the_glossary[label]:
        return None
    return the_glossary[label][key]

#   capitalise first letter
#
def cap_first(toks):
    i = next((n for n in range(len(toks))
                    if type(toks[n]) is defs.TextToken), -1)
    if i >= 0:
        # NB: keep original token list
        toks = toks.copy()
        toks[i] = copy.copy(toks[i])
        toks[i].txt = toks[i].txt[0].upper()
    return toks

#   capitalise all letters
#
def cap_all(toks):
    def f(t):
        if type(t) is defs.TextToken:
            t = copy.copy(t)
            t.txt = t.txt.upper()
        return t
    return [f(t) for t in toks.copy()]

#   modify description of glossary entry:
#   - capitalise first letter
#   - append dot
#
def modify_description(parser, toks):
    toks = cap_first(toks)
    txt = parser.get_text_expanded(toks)
    if txt and txt[-1] not in ('.', '!', '?'):
        toks.append(defs.TextToken(toks[-1].pos, '.', pos_fix=True))
    return toks



import pyperclip
import os
import inspect
import re


def clipboard_copy(s):
    """ Copy a string to clipboard.
        Automatically tries to installs xclip on linux if it fails. """
    call = lambda: pyperclip.copy(s)
    try:
        call()
    except pyperclip.PyperclipException:
        os.system("sudo apt-get install xclip")
        call()

def clipboard_get():
    """ Get clipboard string. """
    return pyperclip.paste()


class _Line:
    def __init__(self, indent, code_str, space_before=0, space_after=0):
        self.indent = indent
        self.code_str = code_str
        self.space_before = space_before
        self.space_after = space_after

class CodeGen:
    """ Tool to help with printing code line by line. """
    indent = " " * 4
    def __init__(self):
        self.lines = []

    def add(self, indent, code_str, space_before=0, space_after=0):
        """ Add a new line. """
        self.lines.append(_Line(indent=indent, code_str=code_str, space_before=space_before, space_after=space_after))

    def generate(self):
        """ Generate a list of formatted code lines by iterating stored _Line instances. """
        lines = ["# -------------------- GENERATED CODE --------------------"]
        for line in self.lines:
            for _ in range(line.space_before):
                lines.append("")
            lines.append(f"{self.indent * line.indent}{line.code_str}")
            for _ in range(line.space_after):
                lines.append("")
        lines.append("# --------------------------------------------------------")
        return lines

    def print(self):
        """ Generate and print copyable code. """
        code = "\n".join(self.generate())
        print(code)
        return code

def args_to_attrs(local_dict):
    """ Print code for a dunder init method to store all arguments as attributes.
        A bit silly, could save time for huge signatures.
        Could be expanded with setting default values if None. """
    codeGen = CodeGen()
    for key, value in local_dict.items():
        if key != "self" and key != "cls":
            codeGen.add(2, f"self.{key} = {key}")
    return codeGen.print()



# class Config:
#     """ Easily read and change attributes with generated code for auto-completion. """
#     def _generate_code(self, cls_name, **kwargs):
#         """ Generate Python code for new class that inherits Config. """
#         code = CodeGen()
#         code.add(0, f"class {cls_name}:")
#         code.add(1, f'""" CLASS CODE GENERATED BY `CodeGen` THROUGH `Config()._generated_code()`. """')
#         code.add(1, f"def __init__(self):")
#         for name, default in kwargs.items():
#             code.add(2, f"self._{name} = {json.dumps(default)}")
#
#         for name, default in kwargs.items():
#             code.add(1, f"@property", 1)
#             code.add(1, f"def {name}(self):")
#             code.add(2, f"return self._{name}")
#
#         args = ", ".join([f"{name}=None" for name in kwargs])
#
#         code.add(1, f"def config(self, {args}):", 1)
#         code.add(2, f"for key, value in locals().items():")
#         code.add(3, f"if key != \"self\" and value is not None:")
#         code.add(4, f"setattr(self, \"_\" + key, value)")
#
#         code.print()



def debug(scope, *evals, printOut=True):
    """
    Easily call eval() on an arbitrary amount of evaluation strings.
    Useful for debugging.

    Example:
        debug(locals(), "value", "value + jumpValue", printOut=True)
        debug(locals())  # Prints all objects in scope

    :param dict scope: Just write locals()
    :param str evals: Variable names with or without operations
    :param printOut: Whether to print directly or not
    :return: A nicely formatted string
    """
    if not evals:
        evals = list(scope.keys())

    lines = []
    n = max([len(string) for string in evals])
    for evalStr in evals:
        lines.append(f"{evalStr:>{n}} = {eval(evalStr, scope)}")
    lines.append("")
    text = "\n".join(lines)
    if printOut:
        print(text)
    return text


def _get_header_from_obj(obj, link=False):
    """ Helper for attributes_to_markdown. """
    if isinstance(obj, type):
        obj_type = "class"
        hashtags = "#### "
    else:
        obj_type = "module"
        hashtags = "## "

    if link:
        hashtags = "#"
    header = f"{hashtags}Attributes of {obj_type} {obj.__name__}"
    if link:
        header = header.replace(" ", "-")
    return header

def _get_attributes(obj):
    """ Helper for attributes_to_markdown. """
    return attributes(obj, from_bases=True)

def attributes_to_markdown(obj, allow_bad_docs=False, printed_objs=None, print_out=True, return_lines=True):
    """ Convert attributes of a given obj to a readme string recursively.
        Returns a string if `print_out` is True, otherwise a list of lines.

        Examples:
            attributes_to_markdown(generallibrary)

            attributes_to_markdown(generallibrary.SigInfo)

        Removed method type as it's very tricky with decorated methods.
        Todo: Tests
        """
    import pandas as pd  # Should tell user to use `pip install generallibrary[md_features]`

    classes = []
    rows = []
    errors = False
    obj_is_class = isinstance(obj, type)

    if printed_objs is None:
        printed_objs = [obj]
    else:
        printed_objs.append(obj)

    for key, attr in _get_attributes(obj).items():
        if is_property := isinstance(attr, property):
            attr = attr.fget
        module = getattr(attr, "__module__", "")
        doc_lines = str(attr.__doc__).split("\n")
        explanation = doc_lines[1 if not doc_lines[0] and len(doc_lines) > 1 else 0]
        explanation = re.sub(r"^ +| +$", "", explanation)
        attr_is_cls = isinstance(attr, type)
        type_name = "property" if is_property else "class" if attr_is_cls else attr.__class__.__name__
        name = key
        attrs_count = 0

        # If attr is a variable
        if not module:
            type_name, explanation = "variable", f"Variable of type '{type_name}'."

        # If attr is a method
        if obj_is_class and type_name == "function":
            type_name = "method"

        if attr_is_cls:
            cls = attr
            attrs = _get_attributes(cls)
            if attrs and cls not in classes and cls is not obj:
                classes.append(cls)
                name = f"[{key}]({_get_header_from_obj(cls, link=True)})"
                attrs_count = len(attrs)

        if not allow_bad_docs and (len(explanation) < 5 or not explanation.endswith(".") or explanation.startswith(":") or explanation.startswith("http")):
            print_link_to_obj(attr)
            print(f"    {explanation}")
            errors = True

        rows.append({
            "Module": module.split(".")[-1],
            "Name":  name,
            "Type": type_name,
            "Attributes": attrs_count,
            "Explanation": explanation,
        })

    if errors:
        raise AttributeError("Encountered atleast one bad docstring, posting links.")

    if rows:
        df = pd.DataFrame(rows)

        if df["Attributes"].sum():
            df["Attributes"].replace(0, "", inplace=True)
        else:
            df.drop(inplace=True, columns="Attributes")

        # if obj_is_class:
            # df.drop(inplace=True, columns="Module")
            # df.sort_values(inplace=True, by=["Name", "Type"])

        df.sort_values(inplace=True, by=["Module", "Name"])

        lines = [_get_header_from_obj(obj), df.to_markdown(index=False)]

        for cls in classes:
            if cls not in printed_objs:
                lines.extend(attributes_to_markdown(cls, allow_bad_docs=allow_bad_docs, printed_objs=printed_objs, print_out=False, return_lines=True))

        text = "\n\n".join(lines)
        if print_out:
            print(text)

        if return_lines:
            return lines
        else:
            return text


# https://stackoverflow.com/questions/26300594/print-code-link-into-pycharms-console
def print_link(file=None, line=None):
    """ Print a link in PyCharm to a line in file.
        Defaults to line where this function was called. """
    if file is None:
        file = inspect.stack()[1].filename
    if line is None:
        line = inspect.stack()[1].lineno
    string = f'File "{file}", line {max(line, 1)}'.replace("\\", "/")
    print(string)
    return string

def print_link_to_obj(obj):
    """ Print a link in PyCharm to a module, function, class, method or property. """
    if isinstance(obj, property):
        obj = obj.fget
    file = inspect.getfile(obj)
    line = inspect.getsourcelines(obj)[1]
    return print_link(file=file, line=line)


from generallibrary.object import attributes



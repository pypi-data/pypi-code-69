
import unittest

from generallibrary.versions import VerInfo, package_is_installed
from generallibrary.code import clipboard_copy, clipboard_get, CodeGen, args_to_attrs, debug, attributes_to_markdown, print_link, print_link_to_obj


class CodeTest(unittest.TestCase):
    @unittest.skipIf(VerInfo().linux, "Clipboard - Couldn't get to work in linux VM, maybe works in normal linux environment.")
    def test_clipboard(self):
        clipboard_copy("foo")
        self.assertEqual("foo", clipboard_get())
        clipboard_copy("bar")
        self.assertEqual("bar", clipboard_get())

    def test_CodeGen(self):
        codeGen = CodeGen()
        codeGen.add(0, "print(5)")
        codeGen.add(0, "print(5)", space_before=1)
        codeGen.add(1, "print(5)", space_after=2)

        self.assertEqual(8, len(codeGen.generate()))
        codeGen.print()

    def test_args_to_attrs(self):
        class _Foo:
            @classmethod
            def testing(cls, a, lot, of, random, values="here"):
                self.assertIn("self.lot = lot", args_to_attrs(locals()))
        _Foo.testing(1, 2, 3, 4)

    def test_debug(self):
        x, y, z = 1, 2, 3
        self.assertIn("y * z + 3 = 9", debug(locals(), "x + y", "y * z + 3", "x", "self"))

    @unittest.skipUnless(package_is_installed("pandas"), "Skip unless pandas is installed.")
    def test_attributes_to_markdown(self):
        attributes_to_markdown(VerInfo, allow_bad_docs=True)
        attributes_to_markdown(unittest, allow_bad_docs=True)

    def test_print_link(self):
        """ Hard to assert these methods truly work without manual check. """
        print_link("../code.py", 23)
        print_link("test_code.py", 23)
        print_link("test_code.py")
        print_link(line=23)
        print_link()

    def test_print_link_to_obj(self):
        self.assertIn("line 8", print_link_to_obj(CodeTest))
        self.assertIn("line 9", print_link_to_obj(CodeTest.test_clipboard))
        self.assertIn("unittest/__init__.py\", line 1", print_link_to_obj(unittest))





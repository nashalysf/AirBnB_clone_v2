#!/usr/bin/python3
"""
TestConsole
"""

import console
import inspect
import unittest

HBNBCommand = console.HBNBCommand


class TestConsoleDoc(unittest.TestCase):
    """ Tests documentation of console file """

    def test_pep8_console(self):
        """Tests that console.py conforms to pep8 style guide"""
        pep8 = pep8.StyleGuide()
        result = pep8.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Got console style errors.")

    def test_console_module_docstring(self):
        """ Test console.py module docstrings """
        self.assertTrue(len(console.__doc__) >= 1,
                        "console file needs docstring")
        self.assertIsNot(console.__doc__, None, "console file needs docstring")

    def test_pep8_console_test(self):
        """ Test that test_console.py conforms to pep8 style guide"""
        pep8 = pep8.Styleguide()
        result = pep8.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "Got console style errors")


if '__name__' == '__main__':
    unittest.main()

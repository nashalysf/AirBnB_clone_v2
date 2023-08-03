#!/usr/bin/python3
"""
TestConsole
"""

import console
import inspect
import pep8
import unittest

HBNBCommand = console.HBNBCommand


class TestConsoleDoc(unittest.TestCase):
    """ Tests documentation of console file """

    def test_pep8_console(self):
        """Tests that console.py conforms to pep8 style guide"""
        pep8 = pep8.StyleGuide()
        result = pep8.check_files(['console.py'])
        self.assertEqual(result.total_erros, 0, "Got console style errors.")

    def test_console_module_docstring(self):
        """ Test console.py module docstrings """
        self.assertTrue(len(console.__doc__) >= 1,
                        "console file needs docstring")
        self.assertIsNot(console.__doc__, None, "console file needs docstring")


if '__name__' == '__main__':
    unittest.main()

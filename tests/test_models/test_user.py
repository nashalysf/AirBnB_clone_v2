#!/usr/bin/python3
""" """
import unittest
import pep8
from tests.test_models.test_base_model import test_basemodel
from models import user
from models.base_model import BaseModel
User = user.User


class TestUserDoc(unittest.TestCase):
    """ Tests documentation of user file """

    def test_pep8_user(self):
        """Tests that user.py conforms to pep8 style guide"""
        pep8 = pep8.StyleGuide()
        result = pep8.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors.")

    def test_user_module_docstring(self):
        """ Test user.py module docstrings """
        self.assertTrue(len(user.__doc__) >= 1,
                        "user file needs docstring")
        self.assertIsNot(user.__doc__, None, "user file needs docstring")

    def test_pep8_user_test(self):
        """ Test that test_console.py conforms to pep8 style guide"""
        pep8 = pep8.Styleguide()
        result = pep8.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors")


if '__name__' == '__main__':
    unittest.main()


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

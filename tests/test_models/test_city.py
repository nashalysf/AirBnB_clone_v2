#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City

import unittest
import pep8


class TestCityDoc(unittest.TestCase):
    """ Tests documentation of city file """

    def test_pep8_city(self):
        """Tests that city.py conforms to pep8 style guide"""
        pep8 = pep8.StyleGuide()
        result = pep8.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors.")

    def test_city_module_docstring(self):
        """ Test city.py module docstrings """
        self.assertTrue(len(city.__doc__) >= 1,
                        "city file needs docstring")
        self.assertIsNot(city.__doc__, None, "city file needs docstring")

    def test_pep8_city_test(self):
        """ Test that test_console.py conforms to pep8 style guide"""
        pep8 = pep8.Styleguide()
        result = pep8.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors")


if '__name__' == '__main__':
    unittest.main()


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

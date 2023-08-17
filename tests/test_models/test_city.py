#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City

import unittest


class test_City(test_basemodel):
    """test city"""

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

    def test_init(self):
        """Test initialization of city class"""
        city = city()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_state_id(self):
        """test type of state_id attribute"""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_name(self):
        """test type of name attribute"""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_str(self):
        """test output of __str__ method"""
        city = City()
        output = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), output)


if '__name__' == '__main__':
    unittest.main()

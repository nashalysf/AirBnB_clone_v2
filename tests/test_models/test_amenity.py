#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
import pep8


class TestAmenityModel(unittest.TestCase):
    """ Tests documentation of amenity file """

    def test_pep8_amenity(self):
        """Tests that amenity.py conforms to pep8 style guide"""
        pep8 = pep8.StyleGuide()
        result = pep8.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors.")

    def test_amenity_module_docstring(self):
        """ Test amenity.py module docstrings """
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity file needs docstring")
        self.assertIsNot(amenity.__doc__, None, "amenity file needs docstring")

    def test_pep8_amenity_test(self):
        """ Test that test_console.py conforms to pep8 style guide"""
        pep8 = pep8.Styleguide()
        result = pep8.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "Got style errors")

    def test_amenity_inheritance(self):
        """Test amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test amenity attributes are set correctyl"""
        amenity = Amenity()
        self.assertEqual(amenity, BaseModel)

    def test_amenity_table_name(self):
        """check tablename is set correctly"""
        self.assertEqual(Amenity.__tablename__, 'amneities')

    def test_amenity_serialize(self):
        """test serializing an Amenoty instance"""
        amenity = Amenity()
        am_dict = amenity.to_dic()
        self.assertEqual(am_dict['__class__'], 'Amenity')

    def test_amenity_relationship(self):
        """Test amenity many-to-many relationship"""
        self.assertEqual(Amenity.place_amenities.property.secondary,
                         place_amenity)


if '__name__' == '__main__':
    unittest.main()


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestState(unittest.TestCase):

    def test_init(self):
        """Test initialization of State class"""
        state = State()
        self.assertEqual(state.name, "")

    def test_name(self):
        """Test name attribute is string"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_str(self):
        """Test output of __str__ method"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), string)

    def test_save(self):
        """Test save method updates __dict__"""
        state = State()
        created_at = state.created_at
        updated_at = state.updated_at
        state.save()
        self.assertNotEqual(created_at, state.created_at)
        self.assertNotEqual(updated_at, state.updated_at)


if __name__ == '__main__':
    unittest.main()

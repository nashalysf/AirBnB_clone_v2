#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
class TestReview(unittest.TestCase):

    def test_init(self):
        """test initialization of review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_place_id(self):
        """test type of place id"""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_user_id(self):
        """test user id"""
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_text(self):
        """test text"""
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_str(self):
        """test string"""
        review = Review()
        output = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), output)

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define Unittest for max_integer([..])"""

    def test_ordered(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([4]), 4)

    def test_floats(self):
        """Test a list containing float values."""
        floats = [1.17, -20, 7.56, 2.08]
        self.assertEqual(max_integer(floats), 7.56)

    def test_ints_floats(self):
        """Test a list of both int and float values."""
        mix = [3, -2.9, 12.9, 4, -7]
        self.assertEqual(max_integer(mix), 12.9)

    def test_char(self):
        """Test a list of characters."""
        char = ['t', 'e', 's', 't']
        self.assertEqual(max_integer(char), 't')

    def test_strings(self):
        """Test a string."""
        string = "unittest is amazing"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        """Test a list of strings."""
        string = ["unit", "test", "is", "cool"]
        self.assertEqual(max_integer(string), "unit")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    if __name__ == "__main__":
        unittest.main()

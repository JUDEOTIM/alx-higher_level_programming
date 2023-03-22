#!/usr/bin/python3
""" Square Test Module
"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare_1st(unittest.TestCase):
    def setUp(self):
        print("Testing Square")

    def test_width(self):
        s1 = Square(4, 5)
        self.assertEqual(s1.size, 4)

    def test_height(self):
        s1 = Square(4, 5)
        self.assertEqual(s1.x, 5)

    def test_no_param(self):
        with self.assertRaises(TypeError):
            s2 = Square()

    def test_1_param(self):
        s3 = Square(3)
        self.assertEqual(s3.size, 3)

    def test_rect_from_base(self):
        self.assertIsInstance(Square(4, 5), Base)

    def test_x(self):
        s3 = Square(4)
        self.assertEqual(s3.x, 0)

    def test_x_2(self):
        s3 = Square(4, 5)
        self.assertEqual(s3.x, 5)

    def test_y(self):
        s3 = Square(4, 5)
        self.assertEqual(s3.y, 0)

    def test_y_2(self):
        s3 = Square(4, 5, 7)
        self.assertEqual(s3.y, 7)

    def test_all_param(self):
        s3 = Square(4, 5, 7, 9)
        self.assertEqual(9, s3.id)

    def test_size_private(self):
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__size

    def test_x_private(self):
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__x

    def test_y_private(self):
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__y

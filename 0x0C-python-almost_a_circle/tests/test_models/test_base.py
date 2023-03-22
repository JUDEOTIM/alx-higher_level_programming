#!/usr/bin/python3
""" Test Base Module
"""


import os
import unittest
from models.base import Base


class TestBase_1st(unittest.TestCase):
    def setUp(self):
        print("Testing Base")

    def test_no_param_1_instance(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_no_param_3_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_with_param(self):
        b1 = Base(3)
        self.assertEqual(b1.id, 3)

    def test_none_param(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 5)

    def test_assign_new_id(self):
        b2 = Base()
        b2.id = 6
        self.assertEqual(b2.id, 6)

    def test_bool_param(self):
        b3 = Base(True)
        self.assertNotEqual(b3.id, False)

    def test_isisnstance(self):
        b4 = Base(5)
        self.assertIsInstance(b4, Base)

    def test_privacy(self):
        with self.assertRaises(AttributeError):
            Base().__nb_objects

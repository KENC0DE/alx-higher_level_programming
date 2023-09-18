#!/usr/bin/python3
"""
    Test Square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test Special Rectangle """

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_0(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
from Ronde import check



class TestPointArea1(TestCase):
    def test_check_Coordinates(self):  # the coordinates are inside the circle exactly in the black area
                                       # quarter I
        radius = 4
        x = 1
        y = 1
        expected = True
        actual = check(4, 1, 1)
        self.assertEqual(expected, actual)


class TestPointArea2(TestCase):
    def test_check(self):  # the coordinates are outside the circle
        radius = 4
        x = 7
        y = 1
        expected = False
        actual = check(4, 7, 1)
        self.assertEqual(expected, actual)


class TestPointArea3(TestCase):
    def test_check(self):
        radius = 0
        x = 0
        y = 0
        expected = False
        actual = check(0, 0, 0)
        self.assertEqual(expected, actual)


class TestPointArea4(TestCase): # the coordinates are in 3rd quarter the white area
    def test_check(self):
        radius = -8
        x = -3
        y = 4
        expected = False
        actual = check(-8, -3, 4)
        self.assertEqual(expected, actual)



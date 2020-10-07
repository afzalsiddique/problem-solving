import unittest
from Algorithm_Course.lab01.contest_c import *



class MyTestCase(unittest.TestCase):
    def test_1(self):
        W = 2
        expected = 5
        actual = num_of_tilings(W)
        self.assertEqual(expected, actual)

    def test_2(self):
        W = 3
        expected = 11
        actual = num_of_tilings(W)
        self.assertEqual(expected, actual)

    def test_3(self):
        W = 7
        expected = 781
        actual = num_of_tilings(W)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

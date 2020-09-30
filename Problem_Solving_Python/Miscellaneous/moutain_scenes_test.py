import unittest

from Miscellaneous.moutain_scenes import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        actual = solution.count_mountain_scenes(25, 5, 5)
        expected = 7770
        self.assertEqual(expected,actual)

    def test_2(self):
        solution = Solution()
        actual = solution.count_mountain_scenes(15, 5, 5)
        expected = 6050
        self.assertEqual(expected,actual)

    def test_3(self):
        solution = Solution()
        actual = solution.count_mountain_scenes(10, 10, 1)
        expected = 1022
        self.assertEqual(expected,actual)

    def test_4(self):
        solution = Solution()
        actual = solution.count_mountain_scenes(4, 2, 2)
        expected = 6
        self.assertEqual(expected,actual)
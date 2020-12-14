import unittest
from leetcode.lc77 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.combine(4, 2)
        expected = sorted([ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.combine(1,1)
        expected = sorted([[1]])
        self.assertEqual(expected, actual)
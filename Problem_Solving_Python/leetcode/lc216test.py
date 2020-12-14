import unittest
from leetcode.lc216 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 7)
        expected = [[1,2,4]]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 9)
        expected = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = solution.combinationSum3(4, 1)
        expected = []
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 2)
        expected = []
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = solution.combinationSum3(9, 45)
        expected = [[1,2,3,4,5,6,7,8,9]]
        self.assertEqual(expected, actual)
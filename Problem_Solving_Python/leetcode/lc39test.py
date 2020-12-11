import unittest
from leetcode.lc39 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2,3,6,7], 7))
        expected = sorted([[2,2,3],[7]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2,3,5], 8))
        expected = sorted([[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2], 1))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_4  (self):
        solution = Solution()
        actual = sorted(solution.combinationSum([1], 1))
        expected = sorted([[1]])
        self.assertEqual(expected, actual)

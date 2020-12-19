import unittest
from leetcode.lc52 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.totalNQueens(4)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.totalNQueens(5)
        expected = 10
        self.assertEqual(expected, actual)




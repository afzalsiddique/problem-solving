import unittest
from leetcode.lc46 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(expected, solution.permute([1,2,3]))

    def test_2(self):
        solution = Solution()
        expected = [[0,1],[1,0]]
        self.assertEqual(expected, solution.permute([0,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual([[1]], solution.permute([1]))

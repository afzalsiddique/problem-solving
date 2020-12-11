import unittest
from leetcode.lc47 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.permuteUnique([1,1,2]))
        expected = sorted([[1,1,2], [1,2,1], [2,1,1]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(expected, solution.permuteUnique([1,2,3]))
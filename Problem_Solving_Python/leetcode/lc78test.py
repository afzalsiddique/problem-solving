import unittest
from leetcode.lc78 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.subsets([1,2,3]))
        expected = sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.subsets([0]))
        expected = sorted([[],[0]])
        self.assertEqual(expected, actual)
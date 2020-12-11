import unittest
from leetcode.lc40 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.combinationSum2([10,1,2,7,6,1,5], 8))
        expected = sorted([
                            [1,1,6],
                            [1,2,5],
                            [1,7],
                            [2,6]
                            ])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.combinationSum2([2,5,2,1,2], 5))
        expected = sorted([
                            [1,2,2],
                            [5]
                            ])
        self.assertEqual(expected, actual)


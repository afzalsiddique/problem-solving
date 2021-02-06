import unittest
from leetcode.lc746iterativedp import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        cost = [10, 15, 20]
        actual = solution.minCostClimbingStairs(cost)
        expected = 15
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        actual = solution.minCostClimbingStairs(cost)
        expected = 6
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        cost = [0,1,1,0]
        actual = solution.minCostClimbingStairs(cost)
        expected = 1
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        cost = [1, 1, 100, 1]
        actual = solution.minCostClimbingStairs(cost)
        expected = 2
        self.assertEqual(expected, actual)

import unittest
from leetcode.lc70 import *

class MyTestClass(unittest.TestCase):
    def test1(self):
        sol = Solution()
        n = 3
        actual = sol.climbStairs(n)
        expected = 3
        self.assertEqual(expected, actual)

    def test2(self):
        sol = Solution()
        n = 4
        actual = sol.climbStairs(n)
        expected = 5
        self.assertEqual(expected, actual)

    def test3(self):
        sol = Solution()
        n = 5
        actual = sol.climbStairs(n)
        expected = 8
        self.assertEqual(expected, actual)

    def test4(self):
        sol = Solution()
        n = 45
        actual = sol.climbStairs(n)
        expected = 1836311903
        self.assertEqual(expected, actual)

import unittest
from leetcode.lc76 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = "AAA..BBC...BA.C"
        t = "ABC"
        actual = solution.minWindow(s, t)
        expected = "BA.C"
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        actual = solution.minWindow(s, t)
        expected = "BANC"
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = "a"
        t = "b"
        actual = solution.minWindow(s, t)
        expected = ""
        self.assertEqual(expected, actual)
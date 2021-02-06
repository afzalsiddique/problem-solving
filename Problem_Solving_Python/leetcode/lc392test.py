import unittest
from leetcode.lc392 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = "abc"
        t = "ahbgdc"
        expected = True
        actual = solution.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = "a"
        t = "a"
        expected = True
        actual = solution.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = "ab"
        t = "a"
        expected = False
        actual = solution.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = "abcdefg"
        t = "abcdefg"
        expected = True
        actual = solution.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = "abc"
        t = "abbcd"
        expected = True
        actual = solution.isSubsequence(s, t)
        self.assertEqual(expected, actual)
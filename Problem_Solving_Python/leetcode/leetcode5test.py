import unittest
from leetcode.leetcode5 import *

class MyTestClass(unittest.TestCase):
    def test_3(self):
        solution = Solution()
        s = "wabcbat"
        actual = solution.longestPalindrome(s)
        expected = "abcba"
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = "babad"
        actual = solution.longestPalindrome(s)
        expected = "bab"
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = "cbbd"
        actual = solution.longestPalindrome(s)
        expected = "bb"
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        s = "a"
        actual = solution.longestPalindrome(s)
        expected = "a"
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        s = "ac"
        actual = solution.longestPalindrome(s)
        expected = "c"
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        s = "aacabdkacaa"
        actual = solution.longestPalindrome(s)
        expected = "aca"
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        s = "abacab"
        actual = solution.longestPalindrome(s)
        expected = "bacab"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
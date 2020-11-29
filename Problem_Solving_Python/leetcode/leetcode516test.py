import unittest
from leetcode.leetcode516 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'bbbab'
        expected = 4
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)

    def test_1(self):
        solution = Solution()
        s = 'cbbd'
        expected = 2
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)

    def test_1(self):
        solution = Solution()
        s = 'abcdef'
        expected = 1
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

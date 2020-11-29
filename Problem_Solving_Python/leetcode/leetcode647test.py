import unittest
from leetcode.leetcode647 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'babbcb'
        actual = solution.countSubstrings(s)
        expected = 9
        self.assertEqual(expected, actual)

    def test_1(self):
        solution = Solution()
        s = "abc"
        actual = solution.countSubstrings(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_1(self):
        solution = Solution()
        s = "aaa"
        actual = solution.countSubstrings(s)
        expected = 6
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

import unittest
from leetcode.leetcode3 import *

class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'abcabcbb'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = 'bbbbbbb'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = 'pwwkew'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = ''
        actual = solution.lengthOfLongestSubstring(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = 'b'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        s = 'abc'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        s = 'abcabc'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
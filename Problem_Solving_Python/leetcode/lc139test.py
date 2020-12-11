import unittest
from leetcode.lc139 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        actual = solution.wordBreak(s, wordDict)
        expected = False
        self.assertEqual(expected, actual)
    def test_2(self):
        solution = Solution()
        s = "ab"
        wordDict = ['a','b']
        actual = solution.wordBreak(s, wordDict)
        expected = True
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        actual = solution.wordBreak(s, wordDict)
        expected = True
        self.assertEqual(expected, actual)
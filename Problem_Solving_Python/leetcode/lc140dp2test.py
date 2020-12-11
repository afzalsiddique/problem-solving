import unittest
from leetcode.lc140dp2 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                      "cats and dog",
                      "cat sand dog"
                    ])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                          "pine apple pen apple",
                          "pineapple pen apple",
                          "pine applepen apple"
                        ])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = "applepineapple"
        wordDict = ["apple", "pine","pineapple"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                            "apple pine apple",
                            "apple pineapple"
                        ])
        self.assertEqual(expected, actual)
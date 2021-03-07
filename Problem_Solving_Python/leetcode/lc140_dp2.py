# https://www.youtube.com/watch?v=WepWFGxiwRs
# accepted
import unittest
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            n = len(s)
            result = []
            for i in range(1, n + 1):
                word = s[:i]
                if word in wordDict:
                    if n == len(word):
                        result.append(word)
                    else:
                        tmp = word_break(s[i:])
                        for item in tmp:
                            result.append(word + " " + item)
            dp[s] = result
            return result

        return word_break(s)


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

    def test_4(self):
        solution = Solution()
        s = "aaaaaaaaaa"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa","aaaaaa"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = [""]
        self.assertEqual(expected, actual)



    def test_5(self):
        solution = Solution()
        s = "mycatsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog","my"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                      "cats and dog",
                      "cat sand dog"
                    ])
        self.assertEqual(expected, actual)
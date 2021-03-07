# Recursive-> https://www.youtube.com/watch?v=hLQYQ4zj0qg
# Iterative-> https://www.youtube.com/watch?v=WepWFGxiwRs
import unittest
from typing import List

class Solution:
    # Recursive -> easier to write and read
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        di = {}
        def helper(s):
            if not s:return True
            if s in wordDict:return True
            if s in di:return di[s]
            for i in range(1, len(s)):
                left=s[:i]
                right=s[i:]
                di[left] = helper(left)
                di[right] = helper(right)
                if di[left] and di[right]:
                    return True
            return False

        return helper(s)

    # Iterative
    def wordBreak_iterative(self, s: str, wordDict: List[str]) -> bool:
        di = {}
        for word in wordDict:
            di[word] = 1
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                word = s[i:j+1]
                if word in di:
                    dp[i][j] = True
                    continue
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] and dp[k+1][j])
        return dp[0][-1]


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

    def test_4(self):
        solution = Solution()
        s = "cars"
        wordDict = ['car','ca','rs']
        actual = solution.wordBreak(s, wordDict)
        expected = True
        self.assertEqual(expected, actual)


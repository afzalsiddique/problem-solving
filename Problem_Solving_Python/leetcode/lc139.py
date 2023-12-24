from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def recur(i):
            if i==n:
                return True
            for word in wordDict:
                length=len(word)
                if n-i<length: continue
                if s[i:i+length]==word and recur(i+length):
                    return True
            return False

        n=len(s)
        return recur(0)


class Solution5:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def startsWith(i, word_i):
            j = 0
            m = len(wordDict[word_i])
            while i < n and j < m and s[i] == wordDict[word_i][j]:
                i += 1
                j += 1
            return j == m

        @cache
        def dp(i):
            if i == n: return True
            for word_i in range(len(wordDict)):
                if startsWith(i, word_i) and dp(i + len(wordDict[word_i])):
                    return True
            return False

        n = len(s)
        return dp(0)
class Solution4:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        di = {}
        def helper(s:str):
            n = len(s)
            if n==0:
                return True
            if s in di:return di[s]
            for word in wordDict:
                if n < len(word):continue
                else:
                    if word == s[:len(word)]:
                        if helper(s[len(word):]):
                            di[s]=True
                            return di[s]
            di[s]=False
            return di[s]
        return helper(s)

class Solution2:
    # Recursive -> easier to write and read
    # Recursive-> https://www.youtube.com/watch?v=hLQYQ4zj0qg
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

class Solution3:
    # Iterative
    # Iterative-> https://www.youtube.com/watch?v=WepWFGxiwRs
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
    def test01(self):
        self.assertEqual(False, get_sol().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    def test02(self):
        self.assertEqual(True, get_sol().wordBreak("ab", ['a','b']))
    def test03(self):
        self.assertEqual(True, get_sol().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    def test04(self):
        self.assertEqual(True, get_sol().wordBreak("cars", ['car','ca','rs']))


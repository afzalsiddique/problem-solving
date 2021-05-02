import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def palindromePairs(self, words):
        # https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
        lookup = {w:i for i,w in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, suf = word[:j], word[j:]
                if pre==pre[::-1] and suf[::-1] != word and suf[::-1] in lookup:
                    res.append([lookup[suf[::-1]], i])
                if j != len(word) and suf==suf[::-1] and pre[::-1] != word and pre[::-1] in lookup:
                    res.append([i, lookup[pre[::-1]]])
        return res

# tle
class Solution2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        m=len(words)
        res = []
        def palindrome(word):
            return word==word[::-1]

        for i in range(m):
            for j in range(i):
                if palindrome(words[j]+words[i]):
                    res.append([j,i])
        for i in reversed(range(m)):
            for j in reversed(range(i)):
                if palindrome(words[i]+words[j]):
                    res.append([i,j])
        return res

class tester(unittest.TestCase):
    def test1(self):
        words = ["abcd","dcba","lls","s","sssll"]
        Output= [[0,1],[1,0],[3,2],[2,4]]
        self.assertEqual(Output,Solution().palindromePairs(words))
    def test2(self):
        words = ["bat","tab","cat"]
        Output= [[0,1],[1,0]]
        self.assertEqual(Output,Solution().palindromePairs(words))
    def test3(self):
        words = ["a",""]
        Output= [[0,1],[1,0]]
        self.assertEqual(Output,Solution().palindromePairs(words))
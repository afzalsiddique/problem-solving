import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# time O(26*n^2)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n,maxx=len(words),0
        counters = []
        for i in range(n):
            counters.append(Counter(words[i]))
        for i in range(n):
            for j in range(i+1,n):
                flag=True
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if counters[i][c] and counters[j][c]:
                        flag=False
                        break
                if flag:
                    maxx=max(maxx,len(words[i])*len(words[j]))
        return maxx

# time O(1000*n^2)
class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        maxx=0
        for i in range(n):
            for j in range(i+1,n):
                temp = set(words[i]).intersection(set(words[j]))
                if not set(words[i]).intersection(set(words[j])):
                    maxx=max(maxx,len(words[i])*len(words[j]))
        return maxx
class tester(unittest.TestCase):
    def test1(self):
        words = ["abcw","baz","foo","bar","xtfn","abcdef"]
        Output= 16
        self.assertEqual(Output,Solution().maxProduct(words))
    def test2(self):
        words = ["a","ab","abc","d","cd","bcd","abcd"]
        Output= 4
        self.assertEqual(Output,Solution().maxProduct(words))
    def test3(self):
        words = ["a","aa","aaa","aaaa"]
        Output= 0
        self.assertEqual(Output,Solution().maxProduct(words))
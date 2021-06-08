import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        res = 0
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                res += 1
        return res

class Solution2:
    # wrong
    def minSteps(self, s: str, t: str) -> int:
        n=len(s)
        count_s = Counter(s)
        count_t = Counter(t)
        ans=0
        for i in range(n):
            a,b=s[i],t[i]
            if a==b: continue
            if count_s[a]<=count_t[a]: continue
            count_s[a]-=1
            count_t[b]-=1
            ans+=1
        return ans

class tester(unittest.TestCase):
    def test1(self):
        s = "bab"
        t = "aba"
        Output= 1
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test2(self):
        s = "leetcode"
        t = "practice"
        Output= 5
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test3(self):
        s = "anagram"
        t = "mangaar"
        Output= 0
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test4(self):
        s = "xxyyzz"
        t = "xxyyzz"
        Output= 0
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test5(self):
        s = "friend"
        t = "family"
        Output= 4
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test6(self):
        s = "gctcxyuluxjuxnsvmomavutrrfb"
        t = "qijrjrhqqjxjtprybrzpyfyqtzf"
        Output= 18
        self.assertEqual(Output,get_sol().minSteps(s,t))
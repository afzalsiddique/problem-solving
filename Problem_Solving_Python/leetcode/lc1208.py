import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        li = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        # print(li)
        begin,end=0,0
        cost=0
        res=0
        while end<n:
            cost+=li[end]
            end+=1
            while cost>maxCost:
                cost-=li[begin]
                begin+=1
            res=max(res,end-begin)
        return res

class tester(unittest.TestCase):
    def test_1(self):
        s = "abcd"; t = "bcdf"; maxCost = 3
        Output= 3
        self.assertEqual(Output,get_sol().equalSubstring(s,t,maxCost))
    def test_2(self):
        s = "abcd"; t = "cdef"; maxCost = 3
        Output= 1
        self.assertEqual(Output,get_sol().equalSubstring(s,t,maxCost))
    def test_3(self):
        s = "abcd"; t = "acde"; maxCost = 0
        Output= 1
        self.assertEqual(Output,get_sol().equalSubstring(s,t,maxCost))
    def test_4(self):
        s,t,maxCost = "abcd", "cdef", 1
        Output= 0
        self.assertEqual(Output,get_sol().equalSubstring(s,t,maxCost))
    def test_5(self):
        s,t,maxCost = "krpgjbjjznpzdfy", "nxargkbydxmsgby", 14
        Output= 4
        self.assertEqual(Output,get_sol().equalSubstring(s,t,maxCost))
    # def test_6(self):

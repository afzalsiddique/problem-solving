import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # kmp. similar to leetcode 28: "implement strStr()"
    def computeLPSArray(self, pat):
        j = 0 # length of the previous longest prefix suffix
        i = 1
        n = len(pat)
        lps=[0]*n
        while i < n:
            if pat[i]== pat[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1] # go back to previous longest prefix suffix
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def pattern_found(self, pat: List[int], txt: List[int],start) -> int:
        lps = self.computeLPSArray(pat)
        m=len(txt)
        j=0
        i=start
        while i<m:
            if txt[i]==pat[j]:
                i+=1
                j+=1
                if j==len(pat):
                    return i-j
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0
        for group in groups:
            res=self.pattern_found(group,nums,start) # nums is dummy (only pointer)
            if res==-1: return False
            start = res+len(group)
        return True


class MyTestCase(unittest.TestCase):
    def test_1(self):
        groups,nums = [[1,-1,-1],[3,-2,0]],  [1,-1,0,1,-1,-1,3,-2,0]
        Output= True
        self.assertEqual(Output, get_sol().canChoose(groups,nums))
    def test_2(self):
        groups,nums = [[10,-2],[1,2,3,4]],  [1,2,3,4,10,-2]
        Output= False
        self.assertEqual(Output, get_sol().canChoose(groups,nums))
    def test_3(self):
        groups,nums = [[1,2,3],[3,4]],  [7,7,1,2,3,4,7,7]
        Output= False
        self.assertEqual(Output, get_sol().canChoose(groups,nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

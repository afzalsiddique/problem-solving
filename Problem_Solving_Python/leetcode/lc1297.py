import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # check out sliding window in the template folder
    # https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/discuss/457577/C%2B%2B-Greedy-approach-%2B-Sliding-window-O(n).
    # https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/discuss/457577/C++-Greedy-approach-+-Sliding-window-O(n)./411614
    def maxFreq(self, s: str, unique_max: int, minSize: int, maxSize: int) -> int:
        n=len(s)
        l,r=0,0
        count=Counter()
        di=Counter()
        unique=0
        while r<n:
            if count[s[r]]==0: unique+=1
            count[s[r]]+=1
            r+=1

            while unique>unique_max or (r-l)>minSize:
                if count[s[l]]==1: unique-=1
                count[s[l]]-=1
                l+=1
            if r-l==minSize: # s=abcabc, minSize=3, maxSize=6, maxLetter=3. abc, abca ,abcab, abcabc, bca, bcab, bcabc, cab, cabc and abc. counting abc is enough
                di[s[l:r]]+=1

        return max(di.values()) if di.values() else 0



class tester(unittest.TestCase):
    def test_1(self):
        s,maxLetters ,minSize,maxSize= "aababcaab", 2,3,4
        Output= 2
        self.assertEqual(Output,get_sol().maxFreq(s,maxLetters,minSize,maxSize))
    def test_2(self):
        s,maxLetters ,minSize,maxSize= "aaaa",   1,   3,   3
        Output= 2
        self.assertEqual(Output,get_sol().maxFreq(s,maxLetters,minSize,maxSize))
    def test_3(self):
        s,maxLetters ,minSize,maxSize= "aabcabcab",   2,   2,   3
        Output= 3
        self.assertEqual(Output,get_sol().maxFreq(s,maxLetters,minSize,maxSize))
    def test_4(self):
        s,maxLetters ,minSize,maxSize= "abcde",   2,   3,   3
        Output= 0
        self.assertEqual(Output,get_sol().maxFreq(s,maxLetters,minSize,maxSize))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
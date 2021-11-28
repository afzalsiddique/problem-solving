import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC++Python-Sliding-Window/556706
    def numberOfSubstrings(self, s):
        return self.at_most(s,3) - self.at_most(s,2)
    def at_most(self,A:str,k:int)->int: # at_most k unique chars
        counter = Counter()
        n=len(A)
        ans=0
        unique_cnt=0
        l=r=0
        while r<n:
            if counter[A[r]]==0: unique_cnt+=1
            counter[A[r]]+=1
            while unique_cnt>k:
                counter[A[l]]-=1
                if counter[A[l]]==0:
                    unique_cnt-=1
                l+=1
            ans+=r-l+1
            r+=1
        return ans
class Solution2:
    # https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise
    def numberOfSubstrings(self, s):
        def valid(): return all(count[ch]>=1 for ch in 'abc')
        n=len(s)
        res = l = r = 0
        count = Counter()
        while r<n:
            count[s[r]]+=1
            while valid():
                count[s[l]]-=1
                l+=1
            res+=l
            r+=1
        return res

class tester(unittest.TestCase):
    def test_1(self):
        s = "abcabc"
        Output= 10
        self.assertEqual(Output,get_sol().numberOfSubstrings(s))
    def test_2(self):
        s = "aaacb"
        Output= 3
        self.assertEqual(Output,get_sol().numberOfSubstrings(s))
    def test_3(self):
        s = "abc"
        Output= 1
        self.assertEqual(Output,get_sol().numberOfSubstrings(s))
    def test_4(self):
        s = "ababbbc"
        Output= 3
        self.assertEqual(Output,get_sol().numberOfSubstrings(s))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
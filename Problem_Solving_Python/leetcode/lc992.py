import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC++Python-Sliding-Window/556706
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        return self.at_most(A,k) - self.at_most(A,k-1)
    def at_most(self,A:List[int],k:int)->int:
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

class tester(unittest.TestCase):
    def testa01(self):
        self.assertEqual(12,get_sol().at_most([1,2,1,2,3], 2))
    def testa02(self):
        self.assertEqual(5,get_sol().at_most([1,2,1,2,3], 1))
    def testa03(self):
        self.assertEqual(13,get_sol().at_most([1,2,1,3,4], 3))
    def testa04(self):
        self.assertEqual(10,get_sol().at_most([1,2,1,3,4], 2))
    def test03(self):
        self.assertEqual(7,get_sol().subarraysWithKDistinct([1,2,1,2,3],2))
    def test04(self):
        self.assertEqual(3,get_sol().subarraysWithKDistinct([1,2,1,3,4], 3))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):

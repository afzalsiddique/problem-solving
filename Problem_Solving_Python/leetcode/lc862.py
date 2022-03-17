import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
    def shortestSubarray(self, A: List[int], k: int) -> int:
        n=len(A)
        res=float('inf')
        deq = deque()
        A = [0]+list(itertools.accumulate(A))
        for i in range(n+1):
            while deq and A[i]-A[deq[0]]>=k:
                res=min(res,i-deq.popleft())
            while deq and A[i]<=A[deq[-1]]:
                deq.pop()
            deq.append(i)
        return -1 if res==float('inf') else res



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().shortestSubarray([1],  1))
    def test02(self):
        self.assertEqual(-1, get_sol().shortestSubarray([1,2],  4))
    def test03(self):
        self.assertEqual(3, get_sol().shortestSubarray([2,-1,2],  3))
    def test04(self):
        self.assertEqual(2, get_sol().shortestSubarray([56,-21,56,35,-9], 61))
    def test05(self):
        self.assertEqual(3, get_sol().shortestSubarray([84,-37,32,40,95], 167))
    def test06(self):
        self.assertEqual(3, get_sol().shortestSubarray([-28,81,-20,28,-29], 89))
    def test07(self):
        self.assertEqual(2, get_sol().shortestSubarray([56,-21,56,35,-9], 61))
    def test08(self):
        self.assertEqual(2, get_sol().shortestSubarray([-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6], 151))
    def test09(self):
        self.assertEqual(2, get_sol().shortestSubarray([37,51,-50,51,100], 151))
    def test10(self):
        self.assertEqual(2, get_sol().shortestSubarray([37,51,-50,51,100,-47], 151))
    def test11(self):
        self.assertEqual(2, get_sol().shortestSubarray([-34,37,51,3,-12,-50,51,100,-47], 151))

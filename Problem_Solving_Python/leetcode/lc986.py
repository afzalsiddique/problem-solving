import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i,j=0,0
        while i<len(A) and j<len(B):
            a_start,a_end=A[i]
            b_start,b_end=B[j]
            # if not min(a_end,b_end)<max(a_start,b_start): # also works
            if a_start<=b_end and b_start<=a_end:
                res.append([max(a_start,b_start),min(a_end,b_end)])
            if a_end<b_end:
                i+=1
            else:
                j+=1
        return res
class Solution2:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def overlapping(end1,start2):
            return start2<=end1
        # step 1: creating a merged sorted list
        li = []
        i,j=0,0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                li.append(A[i])
                i+=1
            else:
                li.append(B[j])
                j+=1
        li.extend(A[i:])
        li.extend(B[j:])

        # step 1 (alternative):
        # li = sorted(li1 + li2)

        # step 2:
        res = []
        n=len(li)
        start1,end1 = li[0]
        for i in range(1,n):
            start2,end2 = li[i]
            if overlapping(end1,start2):
                res.append([start2,min(end1,end2)])
            start1=min(start1,start2)
            end1 = max(end1,end2)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        firstList,secondList = [[0,2],[5,10],[13,23],[24,25]],  [[1,5],[8,12],[15,24],[25,26]]
        Output= [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertEqual(Output, get_sol().intervalIntersection(firstList,secondList))
    def test2(self):
        firstList,secondList = [[1,3],[5,9]],  []
        Output= []
        self.assertEqual(Output, get_sol().intervalIntersection(firstList,secondList))
    def test3(self):
        firstList,secondList = [],  [[4,8],[10,12]]
        Output= []
        self.assertEqual(Output, get_sol().intervalIntersection(firstList,secondList))
    def test4(self):
        firstList,secondList = [[1,7]],  [[3,10]]
        Output= [[3,7]]
        self.assertEqual(Output, get_sol().intervalIntersection(firstList,secondList))
    def test5(self):
        firstList,secondList = [[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]]
        Output= [[4,5],[9,10],[11,12],[14,15],[16,20]]
        self.assertEqual(Output, get_sol().intervalIntersection(firstList,secondList))
    # def test6(self):
    # def test7(self):

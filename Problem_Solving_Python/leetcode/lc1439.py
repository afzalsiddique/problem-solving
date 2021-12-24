import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def getSum(li:tuple[int]):
            res=0
            for i in range(m):
                res+=mat[i][li[i]]
            return res
        def getNext(li:tuple[int]):
            li=list(li)
            res=[]
            for i in range(m):
                if li[i]+1<n:
                    tmp=li[:i]+[li[i]+1]+li[i+1:]
                    res.append(tuple(tmp))
            return res
        m,n=len(mat),len(mat[0])
        vis=set()
        idx=tuple([0 for _ in range(m)])
        vis.add(idx)
        pq=[(getSum(idx),idx)]
        res=float('-inf')
        for i in range(k):
            if not pq: return res
            res,idx=heappop(pq)
            for nIdx in getNext(idx):
                if nIdx not in vis:
                    vis.add(nIdx)
                    heappush(pq,(getSum(nIdx),nIdx))
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, get_sol().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))
    def test2(self):
        self.assertEqual(17, get_sol().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9))
    def test3(self):
        self.assertEqual(9, get_sol().kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7))
    def test4(self):
        self.assertEqual(12, get_sol().kthSmallest(mat = [[1,1,10],[2,2,9]], k = 7))
    # def test5(self):
    # def test6(self):
    # def test7(self):


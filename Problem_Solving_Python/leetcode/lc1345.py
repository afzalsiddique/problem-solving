import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        di=defaultdict(list)
        for i,x in enumerate(arr):
            di[x].append(i)

        res=0
        vis=set()
        q=deque([0])
        while q:
            for _ in range(len(q)):
                i=q.popleft()
                if i in vis: continue
                vis.add(i)
                if i==n-1: return res
                if i+1<n: q.append(i+1)
                if i-1>=0: q.append(i-1)
                while di[arr[i]]: q.append(di[arr[i]].pop()) # add the last index first
            res+=1

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))
    def test2(self):
        self.assertEqual(0, get_sol().minJumps(arr = [7]))
    def test3(self):
        self.assertEqual(1, get_sol().minJumps(arr = [7,6,9,6,9,6,9,7]))
    def test4(self):
        self.assertEqual(2, get_sol().minJumps(arr = [6,1,9]))
    def test5(self):
        self.assertEqual(3, get_sol().minJumps(arr = [11,22,7,7,7,7,7,7,7,22,13]))

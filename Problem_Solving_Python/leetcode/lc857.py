import functools
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class MaxHeap:
    def __init__(self):
        self.li=[]
    def push(self,val): heappush(self.li,-val)
    def pop(self): return heappop(self.li)*(-1)
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        expect=[[w/q,q] for w,q in zip(wage,quality)]
        expect.sort()
        max_heap=MaxHeap()
        q_sum=0
        res=float('inf')
        for i in range(k-1):
            ratio,q=expect[i]

            max_heap.push(q)
            q_sum+=q

        for i in range(k-1,len(quality)):
            ratio,q=expect[i]

            max_heap.push(q)
            q_sum+=q
            res=min(res,ratio*q_sum)
            q_sum-=max_heap.pop()
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        actual = get_sol().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2)
        Output= 105.00000
        self.assertEqual(Output, actual)
    def test2(self):
        actual = get_sol().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3)
        Output= 30.66667
        self.assertEqual(Output, actual)
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):

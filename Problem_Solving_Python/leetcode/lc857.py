import functools
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class MaxHeap:
    def __init__(self):
        self.li=[]
    def push(self,val): heappush(self.li,-val)
    def pop(self): return heappop(self.li)*(-1)
    def __len__(self): return len(self.li)
class Solution:
    # https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)/262756
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        expect=[[w/q,q] for w,q in zip(wage,quality)] # each worker asking for at least expect[i] for each unit of his quality
        expect.sort() # sorted based on wage/quality ratio. ratio will never decrease
        max_heap=MaxHeap()
        q_sum=0 # quality_sum
        res=float('inf')
        for i in range(len(quality)):
            ratio,q=expect[i]

            max_heap.push(q)
            q_sum+=q
            if len(max_heap)>k:
                q_sum-=max_heap.pop() # ratio will never decrease. So remove high quality worker to minimize cost
            if len(max_heap)==k: # select exactly k workers
                res=min(res,ratio*q_sum)
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

import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class MaxHeap:
    def __init__(self):
        self.li=[]
    def __repr__(self):
        return str(self.li)
    def push(self,x):
        heappush(self.li,-x)
    def pop(self):
        return heappop(self.li)*(-1)
    def top(self):
        return self.li[0]*(-1)
    def __len__(self):
        return len(self.li)
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = MaxHeap()
        minn=float('inf')
        res=float('inf')
        for x in nums:
            num = x if x&1==0 else x*2
            minn=min(minn,num)
            pq.push(num)
        while len(pq)!=0 and pq.top()&1==0:
            tmp=pq.top()
            res=min(res,pq.pop()-minn)
            minn=min(minn,tmp//2)
            pq.push(tmp//2)
        if len(pq):
            res=min(res,pq.top()-minn)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minimumDeviation([1,2,3,4]))
    def test2(self):
        self.assertEqual(3, get_sol().minimumDeviation([4,1,5,20,3]))
    def test3(self):
        self.assertEqual(3, get_sol().minimumDeviation([2,10,8]))
    def test4(self):
        self.assertEqual(1, get_sol().minimumDeviation([3,5]))
    # def test5(self):
    # def test6(self):
    # def test7(self):


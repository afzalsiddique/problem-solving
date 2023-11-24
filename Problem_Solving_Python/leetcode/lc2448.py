from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calculate_cost(x):
            return sum(abs(nums[i]-x)*cost[i] for i in range(n))

        n=len(nums)
        if n==1: return 0
        nums,cost=zip(*sorted(zip(nums,cost)))
        res=float('inf')
        l,r=0,n-1
        while l<=r:
            m1=(l+r)//2
            m2=m1+1
            while m2+1<=r and nums[m1]==nums[m2]:
                m2+=1
            while m1-1>=l and nums[m1]==nums[m2]:
                m1-=1
            cost_m1=calculate_cost(nums[m1])
            cost_m2=calculate_cost(nums[m2])
            res=min(res,cost_m1,cost_m2)
            if cost_m1<cost_m2:
                r=m1-1
            else:
                l=m2+1
        return res




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(8,get_sol().minCost([1,3,5,2], [2,3,1,14]))
    def test02(self):
        self.assertEqual(0,get_sol().minCost([2,2,2,2,2], [4,2,8,1,3]))
    def test03(self):
        self.assertEqual(383,get_sol().minCost([6,5,8,2,9,8,8,2,4,8,8,2,1,8,8,6,3,8,9,7,7,9,3,9,4,3,7,5,1,3,6,3,1,2,6], [4,8,7,8,5,2,4,5,8,4,2,2,3,7,5,4,2,3,5,3,5,2,8,5,9,3,6,8,2,8,3,1,8,5,1]))
    # def test04(self):
    # def test05(self):
    # def test06(self):

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            vis = set()
            if nums[i]>0:
                while True:
                    if nums[i]<0: break
                    if abs(nums[i]%n)==0: break # case: -1,-2,-3,-4,-5
                    if i in vis and len(vis)>1: return True
                    if i in vis and len(vis)==1: break
                    vis.add(i)
                    i= (i + nums[i])%n
                    if not 0<=i<n: break
        for i in range(n):
            vis = set()
            if nums[i]<0:
                while True:
                    if nums[i]>0: break
                    if abs(nums[i]%n)==0: break # case: -1,-2,-3,-4,-5
                    if i in vis and len(vis)>1: return True
                    if i in vis and len(vis)==1: break
                    vis.add(i)
                    i= (i + nums[i])%n
                    if not 0<=i<n: break
        return False

class tester(unittest.TestCase):
    def test1(self):
        nums = [2,-1,1,2,2]
        Output= True
        self.assertEqual(Output,get_sol().circularArrayLoop(nums))
    def test2(self):
        nums = [-1,2]
        Output= False
        self.assertEqual(Output,get_sol().circularArrayLoop(nums))
    def test03(self):
        nums = [-2,1,-1,-2,-2]
        Output= False
        self.assertEqual(Output,get_sol().circularArrayLoop(nums))
    def test04(self):
        nums = [-1,-2,-3,-4,-5]
        Output= False
        self.assertEqual(Output,get_sol().circularArrayLoop(nums))

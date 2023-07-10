from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jumps=[0]*(n+1)
        for i in range(n+1):
            idx=max(0,i-ranges[i])
            rightEnd=i+ranges[i]
            jumps[idx]=max(jumps[i],rightEnd-idx)
        return self.jump(jumps)

    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        pos=n-1
        res=0
        while pos:
            newPos=pos
            for i in range(pos):
                if i+nums[i]>=pos:
                    newPos=i
                    res+=1
                    break
            if pos==newPos: return -1
            pos=newPos
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().minTaps(5, [3,4,1,1,0,0]))
    def test02(self):
        self.assertEqual(-1, get_sol().minTaps(3, [0,0,0,0]))
    def test03(self):
        self.assertEqual(3, get_sol().minTaps(7, [1,2,1,0,2,1,0,1]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test8(self):

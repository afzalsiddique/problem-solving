from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def at_most(self,nums,k):
        n=len(nums)
        l=r=0
        count=defaultdict(int)
        unq_cnt=0
        res=0
        while r<n:
            while l<r and unq_cnt>k:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    unq_cnt-=1
                l+=1
            res+=1
            if count[nums[r]]==0:
                unq_cnt+=1
            count[nums[r]]+=1
            r+=1
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans1=self.at_most(nums,k)
        ans2=self.at_most(nums,k-1)
        return ans1-ans2


class tester(unittest.TestCase):
    def testa01(self):
        self.assertEqual(12,get_sol().at_most([1,2,1,2,3], 2))
    def testa02(self):
        self.assertEqual(5,get_sol().at_most([1,2,1,2,3], 1))
    def testa03(self):
        self.assertEqual(13,get_sol().at_most([1,2,1,3,4], 3))
    def testa04(self):
        self.assertEqual(10,get_sol().at_most([1,2,1,3,4], 2))
    def test03(self):
        self.assertEqual(7,get_sol().subarraysWithKDistinct([1,2,1,2,3],2))
    def test04(self):
        self.assertEqual(3,get_sol().subarraysWithKDistinct([1,2,1,3,4], 3))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):

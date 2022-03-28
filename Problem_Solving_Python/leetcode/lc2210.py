from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        prev=-1
        for i in range(1,n-1):
            left=i-1
            right=i+1
            while left>=0 and nums[i]==nums[left]:
                left-=1
            while right<n and nums[i]==nums[right]:
                right+=1
            if 0<=left<n and 0<=right<n:
                if nums[left]>nums[i] and nums[right]>nums[i] or nums[left]<nums[i] and nums[right]<nums[i]:
                    if prev!=nums[i]:
                        res+=1
                    prev=nums[i]
            else:
                prev=-1
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().countHillValley([2,4,1,1,6,5]))
    def test02(self):
        self.assertEqual(0,get_sol().countHillValley([6,6,5,5,4,1]))
    def test03(self):
        self.assertEqual(0,get_sol().countHillValley([1,2,3]))

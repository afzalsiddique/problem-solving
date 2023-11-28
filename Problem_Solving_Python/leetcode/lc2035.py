from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/solutions/1513298/c-meet-in-middle/
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//2
        T=sum(nums)
        # nums.sort()
        left,right=[[] for _ in range(n+1)],[[] for _ in range(n+1)]
        for mask in range(1<<n):
            sz=0
            sum_left,sum_right=0,0
            for i in range(n):
                if (1<<i)&mask:
                    sum_left+=nums[i]
                    sum_right+=nums[i+n]
                    sz+=1
            left[sz].append(sum_left)
            right[sz].append(sum_right)
        for tmp_list in right: tmp_list.sort()

        res=float('inf')
        for sz1 in range(1,n+1):
            sz2=n-sz1
            for a in left[sz1]:
                b=(T-2*a)//2
                r_list=right[sz2]
                idx=bisect_left(r_list,b)
                if idx!=len(r_list): # equal or smallest larger
                    res=min(res,abs(T-2*a-2*r_list[idx]))
                if idx!=0: # greatest smaller
                    idx-=1
                    res=min(res,abs(T-2*a-2*r_list[idx]))
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().minimumDifference([3,9,7,3]))
    def test02(self):
        self.assertEqual(72,get_sol().minimumDifference([-36,36]))
    def test03(self):
        self.assertEqual(0,get_sol().minimumDifference([2,-1,0,4,-2,-9]))
    def test04(self):
        self.assertEqual(1,get_sol().minimumDifference([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]))
    # def test05(self):
    # def test06(self):

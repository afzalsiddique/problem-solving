from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # https://www.youtube.com/watch?v=Dxv_kCAYOk4
        n=len(nums)
        if len(nums)==1 or len(nums)==2: return True
        cnt=0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                if i==1 or nums[i]>=nums[i-2]:
                    nums[i-1]=nums[i]
                    cnt+=1
                else:
                    nums[i]=nums[i-1]
                    cnt+=1
        return cnt<=1
class tester(unittest.TestCase):
    def test1(self):
        nums = [4,2,3]
        Output= True
        self.assertEqual(Output,get_sol().checkPossibility(nums))
    def test2(self):
        nums = [4,2,1]
        Output= False
        self.assertEqual(Output,get_sol().checkPossibility(nums))
    def test3(self):
        nums = [-1,4,2,3]
        Output= True
        self.assertEqual(Output,get_sol().checkPossibility(nums))
    def test4(self):
        nums = [3,4,2,3]
        Output= False
        self.assertEqual(Output,get_sol().checkPossibility(nums))
    def test5(self):
        nums = [1,4,1,2]
        Output= True
        self.assertEqual(Output,get_sol().checkPossibility(nums))
    def test6(self):
        self.assertEqual(True,get_sol().checkPossibility([5,7,1,8]))

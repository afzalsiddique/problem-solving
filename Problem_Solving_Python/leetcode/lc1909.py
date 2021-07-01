import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            tmp=nums.pop(i)
            flag=True
            for j in range(len(nums)-1):
                if nums[j]>=nums[j+1]:
                    flag=False
                    break
            nums.insert(i,tmp)
            if flag: return True
        return False




class tester(unittest.TestCase):
    def test01(self):
        nums = [1,2,10,5,7]
        Output= True
        self.assertEqual(Output,get_sol().canBeIncreasing(nums))
    def test02(self):
        nums = [2,3,1,2]
        Output= False
        self.assertEqual(Output,get_sol().canBeIncreasing(nums))
    def test03(self):
        nums = [1,1,1]
        Output= False
        self.assertEqual(Output,get_sol().canBeIncreasing(nums))
    def test04(self):
        nums = [1,2,3]
        Output= True
        self.assertEqual(Output,get_sol().canBeIncreasing(nums))
    def test05(self):
        nums = [100,21,100]
        Output= True
        self.assertEqual(Output,get_sol().canBeIncreasing(nums))

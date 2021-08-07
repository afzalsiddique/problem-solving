import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=xCsIkPLS4Ls
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD=10**9+7
        res=0
        left,right=0,len(nums)-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                res+=pow(2,right-left,MOD)
                left+=1
            else:
                right-=1
        return res % MOD
class Tester(unittest.TestCase):
    def test_1(self):
        nums,target = [3,5,6,7],9
        Output= 4
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
    def test_2(self):
        nums,target = [3,3,6,8],10
        Output= 6
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
    def test_3(self):
        nums,target = [2,3,3,4,6,7],12
        Output= 61
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
    def test_4(self):
        nums,target = [5,2,4,1,7,6,8],16
        Output= 127
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
    def test_5(self):
        nums,target = [7,10,7,3,7,5,4], 12
        Output= 56
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
    def test_6(self):
        nums,target = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14], 22
        Output= 272187084
        self.assertEqual(Output,get_sol().numSubseq(nums,target))
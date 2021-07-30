import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_ending_here=[0]*n
        max_starting_here=[0]*n
        cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            max_ending_here[i]=cnt
        cnt=0
        for i in reversed(range(n)):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            max_starting_here[i]=cnt

        res=0
        # print(max_ending_here)
        # print(max_starting_here)
        for i in range(n-2):
            res=max(res,max_ending_here[i]+max_starting_here[i+2])
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1,1,0,1]
        Output= 3
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test2(self):
        nums = [0,1,1,1,0,1,1,0,1]
        Output= 5
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test3(self):
        nums = [1,1,1]
        Output= 2
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test4(self):
        nums = [1,1,0,0,1,1,1,0,1]
        Output= 4
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test5(self):
        nums = [0,0,0]
        Output= 0
        self.assertEqual(Output,get_sol().longestSubarray(nums))

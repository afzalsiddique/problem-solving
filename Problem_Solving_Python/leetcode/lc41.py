import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
# constant space
# https://www.youtube.com/watch?v=2QugZILS_Q8
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) # missing number will be in range(1,n+1)
        one_exists=False
        for x in nums:
            if x==1:
                one_exists=True
        if not one_exists:return 1
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1
        for i in range(n):
            idx = abs(nums[i])
            if idx<n:
                nums[idx]=-1*abs(nums[idx])
            else:
                nums[0]= -1 * abs(nums[0])
        for i in range(1,n):
            if nums[i]>0:return i
        if nums[0]>0:return n
        return n+1
class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(items, pos1, pos2): items[pos1], items[pos2] = items[pos2], items[pos1]
        nums.append(0)

        for i in range(len(nums)):
            if nums[i] >= len(nums) or nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)): # make nums[i]=i if exists otherwise nums[i]=0
            while nums[i] != i and nums[i] != nums[nums[i]]:
                swap(nums, i, nums[i])

        for i in range(1, len(nums)):
            if i != nums[i]:
                return i

        return len(nums)

class Solution3:
    # bad solution. linear space
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)# missing number will be in range(1,n+1)
        if n==0:return 1
        sett = set()
        for num in nums:
            if num not in sett:
                sett.add(num)
        for i in range(1,n+1):
            if i not in sett:
                return i
        return n+1 # case: [1,2,3]. This should return 4

class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().firstMissingPositive([1]))
    def test2(self):
        self.assertEqual(4, get_sol().firstMissingPositive([1,2,3]))
    def test3(self):
        self.assertEqual(3, get_sol().firstMissingPositive([1,2,0]))
    def test4(self):
        self.assertEqual(2, get_sol().firstMissingPositive([3,4,-1,1]))
    def test5(self):
        Output= 3
        self.assertEqual(Output, get_sol().firstMissingPositive([1,2,0]))
    def test6(self):
        Output= 2
        self.assertEqual(Output, get_sol().firstMissingPositive([3,4,-1,1]))
    def test7(self):
        Output= 1
        self.assertEqual(Output, get_sol().firstMissingPositive([7,8,9,11,12]))
    def test8(self):
        Output= 2
        self.assertEqual(Output, get_sol().firstMissingPositive([1]))
    def test9(self):
        Output= 2
        self.assertEqual(Output, get_sol().firstMissingPositive([1,1]))

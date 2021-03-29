from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

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

# linear space
class Solution2:
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
        self.assertEqual(2, Solution().firstMissingPositive([1]))
    def test2(self):
        self.assertEqual(4, Solution().firstMissingPositive([1,2,3]))
    def test3(self):
        self.assertEqual(3, Solution().firstMissingPositive([1,2,0]))
    def test4(self):
        self.assertEqual(2, Solution().firstMissingPositive([3,4,-1,1]))

import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.pre_sum=[0]*len(nums)
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            self.pre_sum[i]=pre

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right]-self.pre_sum[left] if left!=0 else self.pre_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                res.append(idx+1)
            else:
                nums[idx]=abs(nums[idx])*(-1)
        return res
class tester(unittest.TestCase):
    def test1(self):
        nums = [4,3,2,7,8,2,3,1]
        Output= [2,3]
        self.assertEqual(Output,Solution().findDuplicates(nums))
    def test2(self):
        nums = [1,1,2]
        Output= [1]
        self.assertEqual(Output,Solution().findDuplicates(nums))
    def test3(self):
        nums = [1]
        Output= []
        self.assertEqual(Output,Solution().findDuplicates(nums))

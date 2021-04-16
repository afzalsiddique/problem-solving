from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List




class Solution:
    def nextGreaterElement(self, num: int) -> int:
        nums = [x for x in str(num)]
        n = len(nums)
        BIG = 2147483647
        found = False
        for k in reversed(range(n)):
            if k==n-1:continue
            if nums[k]<nums[k+1]:
                found=True
                break
        if not found:
            nums.reverse()
        for l in reversed(range(n)):
            if nums[l]>nums[k]:
                nums[l],nums[k]=nums[k],nums[l]
                break
        left,right = k+1,n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        res = int(''.join(nums))
        if res<=num or res>BIG:
            return -1
        return res



class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(21,Solution().nextGreaterElement(12))
    def test2(self):
        self.assertEqual(-1,Solution().nextGreaterElement(21))
    def test3(self):
        self.assertEqual(1243,Solution().nextGreaterElement(1234))
    def test4(self):
        self.assertEqual(230412,Solution().nextGreaterElement(230241))
    def test5(self):
        self.assertEqual(-1,Solution().nextGreaterElement(2147483486))
    def test6(self):
        self.assertEqual(2147483647,Solution().nextGreaterElement(2147483476))

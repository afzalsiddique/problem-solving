from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(n)]
        curr=0
        while len(nums)!=1:
            for _ in range(k-1):
                curr+=1
                if curr==len(nums):
                    curr=0
            nums.pop(curr)
            if curr==len(nums):
                curr=0
        return nums[0]+1



class MyTestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3,Solution().findTheWinner(5,2))
    def test_2(self):
        self.assertEqual(1,Solution().findTheWinner(6,5))
    def test_3(self):
        self.assertEqual(1,Solution().findTheWinner(1,6))
    def test_4(self):
        self.assertEqual(1,Solution().findTheWinner(1,6))

from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List







class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di,n= defaultdict(int), len(nums)
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            di[num]+=1
        for num in di:
            bucket[di[num]].append(num)
        res = []
        for i in reversed(range(n+1)):
            if not bucket[i]:continue
            for item in bucket[i]:
                if k==0:return res
                res.append(item)
                k-=1

        return res
class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,2],Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))

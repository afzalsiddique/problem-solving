import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(mid):
            summ=0
            for num in nums:
                summ+=math.ceil(num/mid)
            return summ<=threshold

        lo=1
        hi=max(nums)
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if feasible(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo
# concise version
class Solution2:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo=1
        hi=max(nums)
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if sum(math.ceil(num/mid) for num in nums)<=threshold:
                hi=mid-1
            else:
                lo=mid+1
        return lo

class tester(unittest.TestCase):
    def test1(self):
        nums = [1,2,5,9]
        threshold = 6
        Output= 5
        self.assertEqual(Output,Solution().smallestDivisor(nums,threshold))
    def test2(self):
        nums = [44,22,33,11,1]
        threshold = 5
        Output= 44
        self.assertEqual(Output,Solution().smallestDivisor(nums,threshold))
    def test3(self):
        nums = [21212,10101,12121]
        threshold = 1000000
        Output= 1
        self.assertEqual(Output,Solution().smallestDivisor(nums,threshold))
    def test4(self):
        nums = [2,3,5,7,11]
        threshold = 11
        Output= 3
        self.assertEqual(Output,Solution().smallestDivisor(nums,threshold))

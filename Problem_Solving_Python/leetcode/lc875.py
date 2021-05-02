import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            cnt=0
            for pile in piles:
                if pile%k:
                    cnt+=pile//k+1
                else:
                    cnt+=pile//k
            return cnt<=h

        lo=1
        hi = max(piles)
        while lo<=hi:
            mid = (lo+hi)//2
            if can_eat_all(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo

    # same but concise
    def minEatingSpeed2(self, piles: List[int], max_time: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo+hi)//2
            time = sum([math.ceil(i/mid) for i in piles])
            if time <= max_time:
                hi=mid-1
            else:
                lo=mid+1
        return lo


class tester(unittest.TestCase):
    def test1(self):
        piles = [3,6,7,11]
        h = 8
        Output= 4
        self.assertEqual(Output,Solution().minEatingSpeed(piles,h))
    def test2(self):
        piles = [30,11,23,4,20]
        h = 5
        Output= 30
        self.assertEqual(Output,Solution().minEatingSpeed(piles,h))
    def test3(self):
        piles = [30,11,23,4,20]
        h = 6
        Output= 23
        self.assertEqual(Output,Solution().minEatingSpeed(piles,h))
    def test4(self):
        piles = [312884470]
        h = 968709470
        Output= 1
        self.assertEqual(Output,Solution().minEatingSpeed(piles,h))
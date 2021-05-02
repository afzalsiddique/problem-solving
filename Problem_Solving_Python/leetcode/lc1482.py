import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], min_bouquets: int, flowers_per_bouquet: int) -> int:
        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days: # if not adjacent
                    flowers = 0
                else:
                    flowers+=1
                    bonquets += flowers // flowers_per_bouquet
                    flowers = flowers % flowers_per_bouquet
            return bonquets >= min_bouquets

        if len(bloomDay) < min_bouquets * flowers_per_bouquet:
            return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



class tester(unittest.TestCase):
    def test1(self):
        bloomDay = [1,10,3,10,2]
        m = 3
        k = 1
        Output= 3
        self.assertEqual(Output,Solution().minDays(bloomDay,m,k))
    def test2(self):
        bloomDay = [1,10,3,10,2]
        m = 3
        k = 2
        Output= -1
        self.assertEqual(Output,Solution().minDays(bloomDay,m,k))
    def test3(self):
        bloomDay = [7,7,7,7,12,7,7]
        m = 2
        k = 3
        Output= 12
        self.assertEqual(Output,Solution().minDays(bloomDay,m,k))
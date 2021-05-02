import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], max_day: int) -> int:
        def valid(max_capacity):
            temp_capacity = max_capacity
            day = 1
            for w in weights:
                if w>temp_capacity:
                    day+=1
                    temp_capacity=max_capacity
                temp_capacity-=w
            return day <= max_day

        lo=max(weights)
        hi = sum(weights)
        while lo<=hi:
            mid = (lo+hi)//2
            if valid(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo
class Solution2:
    def shipWithinDays(self, weights: List[int], max_day: int) -> int:
        def valid(max_capacity):
            temp_capacity = max_capacity
            day = 1
            for w in weights:
                # this line could be removed by initializing lo=max(weights)
                if w > max_capacity: return False
                if w>temp_capacity:
                    day+=1
                    temp_capacity=max_capacity
                temp_capacity-=w
            return day <= max_day

        lo=0
        hi = sum(weights)
        while lo<=hi:
            mid = (lo+hi)//2
            if valid(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo

class tester(unittest.TestCase):
    def test1(self):
        weights = [1,2,3,4,5,6,7,8,9,10]
        D = 5
        Output= 15
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test2(self):
        weights = [3,2,2,4,1,4]
        D = 3
        Output= 6
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test3(self):
        weights = [1,2,3,1,1]
        D = 4
        Output= 3
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test4(self):
        weights = [1]
        D = 1
        Output= 1
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test5(self):
        weights = [500]
        D = 1
        Output= 500
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test6(self):
        weights = [500,500]
        D = 1
        Output= 1000
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
    def test7(self):
        weights = [500,500]
        D = 100
        Output= 500
        self.assertEqual(Output,Solution().shipWithinDays(weights,D))
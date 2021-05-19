import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(max_capacity):
            cnt=0
            temp=0
            for i in range(len(weights)):
                if weights[i]>max_capacity: return False
                if temp+weights[i]<=max_capacity:
                    temp+=weights[i]
                else:
                    cnt+=1 # send this ship
                    temp=0 # empty the ship
                    temp+=weights[i] # load the current weight in the ship
            if temp !=0: cnt+=1
            return cnt<=days

        lo,hi=0,sum(weights)
        while lo<=hi:
            mid=(lo+hi)//2
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
class Solution3:
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
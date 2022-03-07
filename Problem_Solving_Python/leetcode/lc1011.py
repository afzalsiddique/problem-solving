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

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(15,get_sol().shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
    def test02(self):
        self.assertEqual(6,get_sol().shipWithinDays([3,2,2,4,1,4],3))
    def test03(self):
        self.assertEqual(3,get_sol().shipWithinDays([1,2,3,1,1],4))
    def test04(self):
        self.assertEqual(1,get_sol().shipWithinDays([1],1))
    def test05(self):
        self.assertEqual(500,get_sol().shipWithinDays([500],1))
    def test06(self):
        self.assertEqual(1000,get_sol().shipWithinDays([500,500],1))
    def test07(self):
        self.assertEqual(500,get_sol().shipWithinDays([500,500],100))
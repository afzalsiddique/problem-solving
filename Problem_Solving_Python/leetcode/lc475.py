import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # 1. For each house, find its position between those heaters (thus we need the heaters array to be sorted).
    # 2. Calculate the distances between this house and left heater and right heater, get a MIN value of those two
    # values. Corner cases are there is no left or right heater.
    # 3. Get MAX value among distances in step 2. It's the answer. Time
    # complexity: max(O(nlogn), O(mlogn)) - m is the length of houses, n is the length of heaters.
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxx=0
        for house in houses:
            idx = bisect_left(heaters,house)
            temp = float('inf')
            if idx!=0:
                temp = min(temp,abs(house-heaters[idx-1]))
            if idx!=len(heaters):
                temp = min(temp,abs(house-heaters[idx]))
            maxx=max(maxx,temp)
        return maxx
class Solution4:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def canConver(radius:int):
            for house in houses:
                idx=bisect_left(heaters,house)
                if idx<len(heaters) and heaters[idx]==house:
                    continue
                idx=bisect_right(heaters,house)
                if idx<len(heaters) and abs(heaters[idx]-house)<=radius:
                    continue
                idx=bisect_right(heaters,house-radius-1)
                if idx<len(heaters) and abs(house-heaters[idx])<=radius:
                    continue
                return False
            return True

        houses.sort()
        heaters.sort()
        lo,hi=0,max(houses)+max(heaters)
        while lo<=hi:
            m=(lo+hi)//2
            if canConver(m):
                hi=m-1
            else:
                lo=m+1
        return lo
class Solution2:
    # tle
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def feasible(radius):
            for house in houses:
                if not any(abs(house-heater)<=radius for heater in heaters):
                    return False
            return True

        lo=0
        hi=int(1e9)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if feasible(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo
class Solution3:
    # tle
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n=len(houses)
        li=[float('inf') for _ in range(n)]
        for h in heaters:
            for i in range(n):
                li[i]=min(li[i],abs(h-houses[i]))
        return max(li)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().findRadius([1,2,3],[2]))
    def test02(self):
        self.assertEqual(1,get_sol().findRadius([1,2,3,4],[1,4]))
    def test03(self):
        self.assertEqual(3,get_sol().findRadius([1,5],[2]))
    def test04(self):
        self.assertEqual(9,get_sol().findRadius([1,5],[10]))
    def test05(self):
        self.assertEqual(0,get_sol().findRadius([1],[1,2,3,4]))
    def test06(self):
        self.assertEqual(0,get_sol().findRadius([1,2,3], [1,2,3]))
    def test07(self):
        self.assertEqual(498,get_sol().findRadius([1,999], [499,500,501]))
    def test08(self):
        self.assertEqual(498,get_sol().findRadius([1,1,1,1,1,1,999,999,999,999,999], [499,500,501]))

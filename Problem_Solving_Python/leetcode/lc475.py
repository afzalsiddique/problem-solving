import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# 1. For each house, find its position between those heaters (thus we need the heaters array to be sorted).
# 2. Calculate the distances between this house and left heater and right heater, get a MIN value of those two
# values. Corner cases are there is no left or right heater.
# 3. Get MAX value among distances in step 2. It's the answer. Time
# complexity: max(O(nlogn), O(mlogn)) - m is the length of houses, n is the length of heaters.
class Solution:
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
# tle
class Solution2:
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


class tester(unittest.TestCase):
    def test1(self):
        houses = [1,2,3]
        heaters = [2]
        Output= 1
        self.assertEqual(Output,Solution().findRadius(houses,heaters))
    def test2(self):
        houses = [1,2,3,4]
        heaters = [1,4]
        Output= 1
        self.assertEqual(Output,Solution().findRadius(houses,heaters))
    def test3(self):
        houses = [1,5]
        heaters = [2]
        Output= 3
        self.assertEqual(Output,Solution().findRadius(houses,heaters))
    def test4(self):
        houses = [1,5]
        heaters = [10]
        Output= 9
        self.assertEqual(Output,Solution().findRadius(houses,heaters))
    def test5(self):
        houses = [1]
        heaters = [1,2,3,4]
        Output= 0
        self.assertEqual(Output,Solution().findRadius(houses,heaters))
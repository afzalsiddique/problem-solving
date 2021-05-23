import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(nlogn)
    def findMinDifference(self, timePoints: List[str]) -> int:
        n=len(timePoints)
        def convert_to_minutes(timePoint) -> int:
            hours = int(timePoint[:2])
            minutes = int(timePoint[3:])
            return hours*60+minutes

        if n>1440: return 0
        times = sorted([convert_to_minutes(x) for x in timePoints])
        minn=float('inf')
        for i in range(n-1):
            minn=min(minn,times[i+1]-times[i])

        option1 = abs(times[-1]-times[0])
        option2 = abs(1440-option1)
        minn=min(minn,option1,option2)
        return minn
class Solution2:
    # time O(n^2)
    def findMinDifference(self, timePoints: List[str]) -> int:
        n=len(timePoints)
        def convert_to_minutes(timePoint) -> int:
            hours = int(timePoint[:2])
            minutes = int(timePoint[3:])
            return hours*60+minutes

        if n>1440: return 0
        times = [convert_to_minutes(x) for x in timePoints]
        minn=float('inf')
        for i in range(n):
            for j in range(i+1,n):
                option1 = abs(times[i]-times[j])
                option2 = abs(1440-option1)
                minn=min(minn,option1,option2)
        return minn
class tester(unittest.TestCase):
    def test01(self):
        timePoints = ["23:59","00:00"]
        Output= 1
        self.assertEqual(Output, get_sol().findMinDifference(timePoints))
    def test02(self):
        timePoints = ["00:00","23:59","00:00"]
        Output= 0
        self.assertEqual(Output, get_sol().findMinDifference(timePoints))
    def test03(self):
        timePoints = ["22:00","02:00"]
        Output= 240
        self.assertEqual(Output, get_sol().findMinDifference(timePoints))
    def test04(self):
        timePoints = ["00:00","12:00"]
        Output= 720
        self.assertEqual(Output, get_sol().findMinDifference(timePoints))
    def test05(self):
        timePoints = ["00:00","12:01"]
        Output= 719
        self.assertEqual(Output, get_sol().findMinDifference(timePoints))

import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def valid(speed):
            ans=0
            for i in range(len(dist)):
                if i!=len(dist)-1:
                    ans+=math.ceil(dist[i]/speed)
                else:
                    ans+=dist[i]/speed
            return ans

        if len(dist)>math.ceil(hour): return -1
        left,right=1,10**7
        while left<=right:
            mid = left + (right-left)//2
            need = valid(mid)
            if need<=hour:
                right=mid-1
            else:
                left=mid+1
        return left

class MyTestCase(unittest.TestCase):
    def test1(self):
        dist,hour = [1,3,2],  6
        Output= 1
        self.assertEqual(Output, get_sol().minSpeedOnTime(dist,hour))
    def test2(self):
        dist,hour = [1,3,2],  2.7
        Output= 3
        self.assertEqual(Output, get_sol().minSpeedOnTime(dist,hour))
    def test3(self):
        dist,hour = [1,3,2],  1.9
        Output= -1
        self.assertEqual(Output, get_sol().minSpeedOnTime(dist,hour))
    def test4(self):
        dist,hour = [1,1,100000],  2.01
        Output= 10000000
        self.assertEqual(Output, get_sol().minSpeedOnTime(dist,hour))
    def test5(self):
        dist,hour = [5,3,4,6,2,2,7],  10.92
        Output= 4
        self.assertEqual(Output, get_sol().minSpeedOnTime(dist,hour))
    # def test6(self):
    # def test7(self):

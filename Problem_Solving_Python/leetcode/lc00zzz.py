import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697703/greedy-with-a-heap/589617
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        rainy_days=defaultdict(deque)
        nearest_flooding=[]
        res=[-1]*n
        for i in range(n):
            lake_no=rains[i]
            if lake_no==0: continue
            day=i
            rainy_days[lake_no].append(day)

        for i in range(n):
            lake_no=rains[i]
            today=i

            if lake_no!=0: # raining in lake_no lake
                if nearest_flooding and nearest_flooding[0][0]==today:
                    return []

                rainy_days[lake_no].popleft() # just rained in lake_no. so pop out
                if rainy_days[lake_no]: # if it will rain in lake_no lake in future
                    next_rainy_day = rainy_days[lake_no][0]
                    heappush(nearest_flooding,(next_rainy_day,lake_no))
            else: # dry day
                if not nearest_flooding: # drying out already dried out lake
                    res[i]=1
                else:
                    next_rainy_day,wet_lake=heappop(nearest_flooding)
                    res[i]=wet_lake
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        rains = [1,2,3,4]
        Output= [-1,-1,-1,-1]
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    def test_2(self):
        rains = [1,2,0,0,2,1]
        Output= [-1,-1,2,1,-1,-1]
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    def test_3(self):
        rains = [1,2,0,1,2]
        Output= []
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    def test_4(self):
        rains = [69,0,0,0,69]
        Output= [-1,1,1,69,-1]
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    def test_5(self):
        rains = [10,20,20]
        Output= []
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    def test_6(self):
        rains = [1,0,2,0,2,1]
        Output= [-1,1,-1,2,-1,-1]
        self.assertEqual(Output,get_sol().avoidFlood(rains))
    # def test_7(self):
    # def test_8(self):

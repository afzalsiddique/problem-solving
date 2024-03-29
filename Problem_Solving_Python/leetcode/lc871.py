from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution3()
class Solution3:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        i = 0
        distanceTravelled = 0
        n = len(stations)
        max_heap = [-startFuel]
        stationCount=0
        while max_heap:
            curFuel = heappop(max_heap)*(-1) # max heap
            distanceTravelled += curFuel
            if distanceTravelled >= target:
                return stationCount
            while i < n and stations[i][0] <= distanceTravelled:
                heappush(max_heap,-stations[i][1])
                i+=1
            # for i in range(n): # wrong. because taking fuel from the same station multiple times
            #     if stations[i][0]<=distanceTravelled:
            #         heappush(max_heap,-stations[i][1])
            stationCount+=1
        return -1
class Solution:
    # https://www.youtube.com/watch?v=4RgqAQFr9WQ
    # not good. O(n^2)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp[t] means the furthest distance that we can get with t times of refueling.
        n=len(stations)
        dp=[0]*(n+1)
        dp[0]=startFuel

        for i in range(n):
            for no_of_refill in range(i,-1,-1): # for i=2 station, we can refuel 0 times, 1 time or 2 times
                if dp[no_of_refill]<stations[i][0]: # it is impossible to reach the current station
                    break
                dp[no_of_refill+1]=max(dp[no_of_refill+1],dp[no_of_refill]+stations[i][1])

        for i,x in enumerate(dp):
            if x>=target: return i
        return -1
class Solution2:
    # tle
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([0,startFuel])
        stations.sort()
        positions=[x[0] for x in stations]
        fuels = [x[1] for x in stations]

        q=deque([(0,startFuel)])
        res=0
        while q:
            for _ in range(len(q)):
                pos1,fuel1 = q.popleft()
                if pos1+fuel1>=target: return res
                left=bisect_right(positions,pos1)
                right=bisect_right(positions,pos1+fuel1)
                for i in range(left,right):
                    q.append((positions[i],fuel1+fuels[i]-(positions[i]-pos1)))
            res+=1
        return -1


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, get_sol().minRefuelStops(target = 1, startFuel = 1, stations = []))
    def test2(self):
        self.assertEqual(-1, get_sol().minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
    def test3(self):
        self.assertEqual(2, get_sol().minRefuelStops(100,10,[[10,60],[20,30],[30,30],[60,40]]))
    def test4(self):
        self.assertEqual(5, get_sol().minRefuelStops(1000,299,[[26,115],[100,47],[444,198],[608,190],[636,157]]))
    def test5(self):
        self.assertEqual(32, get_sol().minRefuelStops(1000, 36, [[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]]))
    def test6(self):
        self.assertEqual(1, get_sol().minRefuelStops(100, 50, [[50,50]]))
    def test7(self):
        self.assertEqual(1, get_sol().minRefuelStops(100, 50, [[25,25],[50,50]]))
    def test8(self):
        self.assertEqual(1, get_sol().minRefuelStops(100, 50, [[25,50],[50,25]]))
    def test9(self):
        self.assertEqual(-1, get_sol().minRefuelStops(100, 50, [[25,30]]))
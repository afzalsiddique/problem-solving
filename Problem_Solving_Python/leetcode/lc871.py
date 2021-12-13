import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=4RgqAQFr9WQ
    # not good. O(n^2)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n=len(stations)
        dp=[0]*(n+1)
        dp[0]=startFuel

        for i in range(n):
            for j in range(i,-1,-1):
                if dp[j]<stations[i][0]: break
                dp[j+1]=max(dp[j+1],dp[j]+stations[i][1])

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
        self.assertEqual(2, get_sol().minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
    def test4(self):
        self.assertEqual(5, get_sol().minRefuelStops(1000,299,[[26,115],[100,47],[444,198],[608,190],[636,157]]))
    def test5(self):
        self.assertEqual(5, get_sol().minRefuelStops(1000, 36, [[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]]))
    # def test6(self):
    # def test7(self):

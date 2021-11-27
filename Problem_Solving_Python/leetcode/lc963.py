import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def dist(x1,y1,x2,y2):
            x,y=abs(x1-x2),abs(y1-y2)
            return sqrt(x*x+y*y)
        def get_area(x1,y1,x2,y2,x3,y3):
            return dist(x1,y1,x2,y2)*dist(x1,y1,x3,y3)

        n=len(points)
        di = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                length = dist(*points[i],*points[j])
                cen_x,cen_y = (points[i][0]+points[j][0])/2, (points[i][1]+points[j][1])/2
                di[length, cen_x,cen_y].append((i,j))

        res = float('inf')
        for key in di:
            lines = di[key]
            if len(lines)<2: continue
            for i in range(len(lines)):
                for j in range(i+1,len(lines)):
                    # three vertices. three vertices are enough to find area
                    p1,p2,p3 = points[lines[i][0]],points[lines[j][0]],points[lines[j][1]]
                    res = min(res,get_area(*p1,*p2,*p3))

        return 0 if res==float('inf') else res


class MyTestCase(unittest.TestCase):
    def test1(self):
        points = [[1,2],[2,1],[1,0],[0,1]]
        Output= 2.00000
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test2(self):
        points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
        Output= 1.00000
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test3(self):
        points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
        Output= 0
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test4(self):
        points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
        Output= 2.00000
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test5(self):
        points = [[83,10945],[18601,28546],[11566,8764],[2962,3913],[16231,8121],[11445,1460],[14735,19151],[8615,10167],[10339,18652],[11535,8580],[21136,20346],[1979,18819],[14140,6865],[12868,17924],[3044,16889],[2618,9195],[15178,21225],[11930,20964],[13990,155],[6663,7648],[23506,23127],[15660,1163],[15470,4696],[17698,7224],[542,11754],[14823,5539],[4894,2434],[3621,4213],[9610,10741],[3051,11981],[27983,8313],[17251,1950],[6208,17938],[3179,10631],[4381,2540],[7330,14161],[11226,18947],[11757,18203],[7918,18067],[15120,23243],[15628,9052],[15340,7705],[13107,11827],[13537,12725],[12588,26956],[12983,7860],[10948,11425],[6278,12204],[11387,16222],[4703,1557]]
        Output= 42836625.0
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test6(self):
        points = [[17620,15918],[16557,17380],[14306,5380],[8122,16595],[20699,22353],[8012,13547],[16677,5186],[5442,18430],[19682,18657],[11330,17502],[12485,10909],[16907,22558],[9893,13834],[1892,7084],[11405,17334],[17681,12670],[7958,2664],[25618,10159],[6233,14819],[10897,16584],[12260,4593],[25361,17103],[16848,13659],[3219,17126],[12903,11950],[9824,17437],[14044,8942],[4991,11384],[6182,4970],[6626,8491],[8932,19987],[13641,11555],[13721,14837],[13439,2255],[7418,9989],[5168,7114],[13821,2993],[10800,18811],[13386,21856],[20414,13028],[5821,6072],[3098,5014],[13117,11848],[13084,8390],[17686,9547],[23956,10159],[5625,6038],[1298,6004],[2763,4664],[1635,4848]]
        Output= 0
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))
    def test7(self):
        points = [[9598,8577],[20322,5440],[6455,9858],[9102,3823],[11908,988],[12797,10913],[18878,20617],[13673,748],[8387,18160],[9289,5308],[10764,15011],[6461,4848],[10068,5389],[6728,24905],[9516,8515],[10060,8808],[2584,9785],[18113,9275],[13437,11520],[19613,12050],[3129,5746],[7814,10846],[8204,15126],[15247,14410],[13932,13906],[16459,14127],[27041,6957],[14960,16973],[7043,207],[10719,10476],[20767,18975],[19049,2395],[746,6996],[11563,12291],[12681,9540],[6724,13393],[9218,11459],[20428,16400],[12130,21131],[7176,13676],[22,8630],[7328,17859],[17725,14503],[19784,10784],[9533,3467],[8269,5675],[18345,8481],[1082,14957],[2205,12328],[1322,17167]]
        Output= 62202920.0
        self.assertEqual(Output, get_sol().minAreaFreeRect(points))

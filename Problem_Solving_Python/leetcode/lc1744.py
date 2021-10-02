import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canEat(self, candies: List[int], queries: List[List[int]]) -> List[bool]:
        pre=[0]+list(itertools.accumulate(candies))
        res=[]
        for type, day, cap in queries:
            mx = pre[type+1]-1
            mn = pre[type]//cap
            if mn<=day<=mx:
                res.append(True)
            else:
                res.append(False)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        candiesCount,queries = [7,4,5,3,8],  [[0,2,2],[4,2,4],[2,13,1000000000]]
        Output= [True,False,True]
        self.assertEqual(Output, get_sol().canEat(candiesCount, queries))
    def test2(self):
        candiesCount,queries = [5,2,6,4,1],  [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
        Output= [False,True,True,False,False]
        self.assertEqual(Output, get_sol().canEat(candiesCount, queries))
    def test3(self):
        candiesCount,queries = [10,11,42,42,49,14,44,33,13,49,32,19,48,36,25,38,32,45,30,21,13,45,39,12,12,25,26,18,35,28,1,31,14,16,38,49,26,33,39,39,7,31,20,8,49,36,6,1,32,2,35,10,31,37,13,43,26], [[24,579,17],[13,275,40],[38,432,75],[47,62,4],[14,908,33],[19,1031,77],[18,316,71],[54,1558,48],[35,1403,19],[10,449,58],[0,1258,94],[41,1014,59],[33,932,15],[18,1488,46],[51,630,89],[7,362,4],[1,14,3],[0,1029,3],[2,1454,63],[52,19,44],[7,418,18],[42,1505,12],[49,1188,92],[15,1116,76],[47,668,40],[50,468,7],[49,167,8],[51,316,94],[27,1270,58],[1,158,66],[25,979,28],[11,837,84],[27,1311,80],[16,1148,77],[51,1538,34],[19,120,70],[8,1508,7],[24,1464,93],[1,1448,44],[45,331,12],[17,111,4],[6,332,19],[53,1368,98],[23,609,85],[11,1364,69],[54,1066,32],[8,1566,30],[40,1331,21],[16,1478,23],[34,133,65],[17,1484,9],[37,1150,65],[13,885,69],[54,191,46],[21,105,22],[1,37,75],[35,479,79],[37,905,89],[49,551,74],[16,986,26],[21,1325,34],[41,1520,67],[40,611,69],[7,997,22],[32,1108,39],[2,1549,59],[35,553,71],[28,729,93],[15,357,11],[43,566,90],[18,1213,87],[23,10,100],[8,423,18],[19,1270,59],[15,413,64],[44,765,76],[5,17,97],[42,1228,10],[27,1236,44],[5,411,46],[54,458,93],[27,1148,33],[20,429,85],[12,315,88],[56,446,26]]
        Output= [True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,True]
        self.assertEqual(Output, get_sol().canEat(candiesCount, queries))
    # def test4(self):

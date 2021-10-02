import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def get_distance(x1,x2,y1,y2): # euclidean distance
            dx,dy=abs(x1-x2),abs(y1-y2)
            return math.sqrt(dx*dx+dy*dy)
        def get_quality(q, distance):
            if distance<=radius:
                return q//(1+distance)
            return 0

        highest_quality=float('-inf')
        res_x,res_y=(0,0)
        for x1 in range(50+1):
            for y1 in range(50+1):
                tmp=0
                for x2,y2,q in towers:
                    tmp+= get_quality(q,get_distance(x1,x2,y1,y2))
                if tmp>highest_quality:
                    highest_quality=tmp
                    res_x,res_y = x1,y1
                # if (x1,y1) in [(25,29),(16,37)]:
                #     print('x:',x1,' y:',y1,' q:',tmp)
        return [res_x,res_y]


class MyTestCase(unittest.TestCase):
    def test1(self):
        towers = [[1,2,5],[2,1,7],[3,1,9]]
        radius = 2
        Output= [2,1]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))
    def test2(self):
        towers = [[23,11,21]]
        radius = 9
        Output= [23,11]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))
    def test3(self):
        towers = [[1,2,13],[2,1,7],[0,1,9]]
        radius = 2
        Output= [1,2]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))
    def test4(self):
        towers = [[2,1,9],[0,1,9]]
        radius = 2
        Output= [0,1]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))
    def test5(self):
        towers = [[42,0,0]]
        radius = 7
        Output= [0,0]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))
    def test6(self):
        towers = [[45,12,4],[13,21,27],[31,17,40],[25,29,45],[37,29,25],[16,37,48],[4,3,31]]
        radius = 42
        Output= [16,37]
        self.assertEqual(Output, get_sol().bestCoordinate(towers,radius))


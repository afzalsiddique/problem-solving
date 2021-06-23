import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n==1: return 1
        li = []
        for i in range(n):
            di=defaultdict(int)
            for j in range(n):
                if i==j: continue
                x1,y1,x2,y2=points[i][0],points[i][1],points[j][0],points[j][1]
                if x2-x1==0:
                    slope = float('inf')
                else:
                    slope = (y2-y1)/(x2-x1)
                di[slope]+=1
            li.append(max(di.values())+1)
        return max(li)

class tester(unittest.TestCase):
    def test01(self):
        points = [[1,1],[2,2],[3,3]]
        Output= 3
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test02(self):
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        Output= 4
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test03(self):
        points = [[1,1]]
        Output= 1
        self.assertEqual(Output,get_sol().maxPoints(points))

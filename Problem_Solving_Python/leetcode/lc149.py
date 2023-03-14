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

class Solution2:
    # not good
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n<2: return n
        di = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if i==j: continue
                x1,y1=points[i]
                x2,y2=points[j]
                delX,delY=x2-x1,y2-y1
                if delY==0:
                    eq='y='+str(y1)
                elif delX==0:
                    eq='x='+str(x1)
                else:
                    m = delY/delX
                    c = y1 - m * x1
                    eq = 'y='+str(m)+'x'+'+'+str(c)
                di[eq].add(tuple(points[i]))
                di[eq].add(tuple(points[j]))
        return max(len(val) for val in di.values())
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().maxPoints([[1,1],[2,2],[3,3]]))
    def test02(self):
        self.assertEqual(4,get_sol().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    def test03(self):
        self.assertEqual(1,get_sol().maxPoints([[1,1]]))
    def test04(self):
        self.assertEqual(3,get_sol().maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]))
    def test05(self):
        self.assertEqual(3,get_sol().maxPoints([[2,3],[3,3],[-5,3]]))
    def test06(self):
        self.assertEqual(5,get_sol().maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dist(x1,y1,x2,y2):
            dx=abs(x2-x1)
            dy=abs(y2-y1)
            ans=dx*dx+dy*dy
            return ans
        def can_reach(i,j):
            x1,y1,r1=bombs[i]
            x2,y2,r2=bombs[j]
            d=dist(x1,y1,x2,y2)
            if d<=r1*r1:
                return True
            return False
        def dfs(u,vis):
            if u in vis: return 0
            vis.add(u)
            ans=1
            for v in g[u]:
                ans+=dfs(v,vis)
            return ans

        n=len(bombs)
        g=defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if can_reach(i,j):
                    g[i].append(j)
                if can_reach(j,i):
                    g[j].append(i)
        print(g)

        res=float('-inf')
        for i in range(n):
            res=max(res,dfs(i,set()))
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().maximumDetonation(bombs = [[2,1,3],[6,1,4]]))
    def test2(self):
        self.assertEqual(1, get_sol().maximumDetonation(bombs = [[1,1,5],[10,10,5]]))
    def test3(self):
        self.assertEqual(5, get_sol().maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
    def test4(self):
        self.assertEqual(1, get_sol().maximumDetonation(bombs = [[1,1,100000],[100000,100000,1]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

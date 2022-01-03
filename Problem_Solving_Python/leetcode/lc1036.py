import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(src:List[int], tar:List[int]):
            q=deque([(src[0],src[1])])
            vis={(src[0],src[1])}
            while q:
                for _ in range(len(q)):
                    x,y=q.popleft()
                    if [x,y]==tar:
                        return True
                    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                        newX,newY=x+dx,y+dy
                        if not 0<=newX<10**6 or not 0<=newY<10**6: continue
                        if (newX,newY)in vis: continue
                        if (newX,newY) in blocked: continue
                        q.append((newX,newY))
                        vis.add((newX,newY))
                        if len(vis)>20000:
                            return True
            return False

        blocked = set((x,y) for x,y in blocked)
        return bfs(source, target) and bfs(target, source)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(False, get_sol().isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
    def test2(self):
        self.assertEqual(True, get_sol().isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))
    def test3(self):
        self.assertEqual(False, get_sol().isEscapePossible([[0,999991],[0,999993],[0,999996],[1,999996],[1,999997],[1,999998],[1,999999]], [0,999997], [0,2]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):

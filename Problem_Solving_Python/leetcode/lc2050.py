from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # topological sort + bfs
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g=defaultdict(list)
        incoming=[0]*n
        dist=time[:] # max time to take the course
        for u,v in relations:
            u-=1;v-=1
            g[u].append(v)
            incoming[v]+=1


        q=deque(u for u in range(n) if incoming[u]==0)
        while q: # level by level is not required
            u=q.popleft()
            for v in g[u]:
                incoming[v]-=1
            for v in g[u]:
                dist[v]=max(dist[v],dist[u]+time[v])
                if not incoming[v]:
                    q.append(v)
        return max(dist)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, get_sol().minimumTime(3,[[1,3],[2,3]], [3,2,5]))
    def test2(self):
        self.assertEqual(12, get_sol().minimumTime( 5, [[1,5],[2,5],[3,5],[3,4],[4,5]],  [1,2,3,4,5]))
    def test3(self):
        self.assertEqual(14, get_sol().minimumTime(5,[[1,2],[1,3]], [7,7,4,5,14]))
    def test4(self):
        self.assertEqual(32, get_sol().minimumTime(9, [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]], [9,5,9,5,8,7,7,8,4]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

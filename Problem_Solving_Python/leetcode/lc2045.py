from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # dijkstra with two minimum distances to a node
    # relaxation is not required because all edge costs are same
    def secondMinimum(self, n: int, E: List[List[int]], time: int, change: int) -> int:
        def updateTime(curTime): # if red wait until green
            greenSignal=curTime//change%2==0
            if greenSignal: return curTime
            return ((curTime+change)//change)*change
        g=defaultdict(list)
        for a,b in E:
            a-=1;b-=1
            g[a]+=[b]
            g[b]+=[a]

        D = [[] for _ in range(n)] # store two minimum distances
        D[0]=[0]
        pq=[(0,0)] # timePassed,node
        while pq:
            curTime,u=heappop(pq)
            if u==n-1 and len(D[u])==2:
                return max(D[u])
            curTime=updateTime(curTime)
            newTime=curTime+time
            for v in g[u]:
                if not D[v] or (len(D[v])==1 and D[v]!=[newTime]): # len(D[v])==1 -> store at most two candidates
                    D[v] += [newTime]
                    heappush(pq,(newTime,v))
class Solution2:
    # tle
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def updateTime(curTime): # if red wait until green
            greenSignal=curTime//change%2==0
            if greenSignal: return curTime
            return ((curTime+change)//change)*change

        g=defaultdict(list)
        for ii,jj in edges:
            ii-=1;jj-=1
            g[ii].append(jj)
            g[jj].append(ii)

        res=float('inf')
        minAlreadyFound=False
        q=deque()
        q.append((0,0)) # node, time
        vis=set()
        vis.add((0,0))
        while q:
            u,curTime=q.popleft()
            vis.add((u,curTime))
            if u==n-1:
                if minAlreadyFound and curTime!=res:
                    return curTime
                if not minAlreadyFound:
                    minAlreadyFound=True
                    res=curTime

            curTime=updateTime(curTime)
            for v in g[u]:
                if (v,curTime+time) not in vis:
                    q.append((v,curTime+time))


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(13, get_sol().secondMinimum( 5,  [[1,3],[1,4],[3,4],[4,5]], 3, 5))
    def test2(self):
        self.assertEqual(11, get_sol().secondMinimum(2, [[1,2]], 3,  2))
    def test3(self):
        self.assertEqual(13, get_sol().secondMinimum( 5,  [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
    def test4(self):
        self.assertEqual(360, get_sol().secondMinimum(12, [[1,2],[1,3],[3,4],[2,5],[4,6],[2,7],[1,8],[5,9],[3,10],[8,11],[6,12]], 60, 600))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

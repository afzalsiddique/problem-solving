import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# We can use BFS Topological Sort to visit the nodes. When visiting the next node, we can forward the color
# information to the next node. Also Topo-sort can help detect circle. One modification is that, for each node,
# we need to store a int cnt[26] array where cnt[i] is the maximum count of color i in all paths to the current node.
# For example, assume there are two paths reaching the current node, aba, bba. Then cnt['a'] = 2 and cnt['b'] = 2
# because both color a and b can be 2 in different paths.
class Solution:
    # concise version
    # bfs topological sort
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        inDegrees, g = [0]*n, [[] for _ in range(n)]
        for _, v in edges: inDegrees[v]+=1
        for u, v in edges: g[u].append(v)
        st = [u for u in range(n) if inDegrees[u]==0]
        cnts = [[0]*26 for _ in range(n)]

        while st: # level by level is not necessary. stack or queue both can do the job
            u = st.pop()
            cnts[u][ord(colors[u])-ord('a')] += 1
            for v in g[u]:
                cnts[v] = list(map(max, cnts[v], cnts[u])) # forward the color information to the next node.
                inDegrees[v] -= 1
                if inDegrees[v]==0: st.append(v)

        return -1 if sum(inDegrees)>0 else max([max(node) for node in cnts])
class Solution2:
    # bfs topological sort
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        g=defaultdict(list)
        cnts=[[0]*26 for _ in range(n)]
        inDegrees=[0 for _ in range(n)]
        for u,v in edges: g[u].append(v)
        for _,v in edges: inDegrees[v]+=1
        st = [u for u in range(n) if inDegrees[u]==0]

        res=float('-inf')
        seen=0
        while st:
            u=st.pop() # level by level is not necessary. stack or queue both can do the job
            cnts[u][ord(colors[u])-ord('a')] += 1
            seen+=1
            res=max(res,max(cnts[u]))
            for v in g[u]:
                for i in range(26):
                    cnts[v][i] = max(cnts[v][i], cnts[u][i]) # forward the color information to the next node.
                inDegrees[v]-=1
                if inDegrees[v]==0:
                    st.append(v)
        return res if seen==n else -1

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().largestPathValue( "abaca", [[0,1],[0,2],[2,3],[3,4]]))
    def test2(self):
        self.assertEqual(-1,get_sol().largestPathValue("a", [[0,0]]))
    def test3(self):
        self.assertEqual(3,get_sol().largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]))
    def test4(self):
        self.assertEqual(26,get_sol().largestPathValue("qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq", [[0,1],[1,2],[2,3],[3,4],[3,5],[4,5],[3,6],[5,6],[6,7],[5,7],[3,7],[6,8],[5,8],[4,8],[8,9],[9,10],[10,11],[9,11],[9,12],[11,12],[6,12],[11,13],[9,13],[13,14],[12,14],[10,14],[11,14],[13,15],[14,15],[12,16],[9,16],[7,16],[15,17],[13,17],[17,18],[11,18],[17,19],[18,19],[13,19],[17,20],[18,20],[19,21],[17,21],[12,22],[21,22],[16,22],[22,23],[21,23],[16,24],[22,24],[15,25],[24,25],[20,25],[12,25],[23,26],[26,27],[13,27],[27,28],[21,28],[26,28],[28,29],[15,30],[27,30],[24,30],[21,30],[27,31],[30,31],[25,32],[29,32],[17,33],[31,33],[32,33],[25,34],[33,35],[31,35],[34,35],[30,36],[35,37],[36,37],[26,38],[36,38],[34,38],[37,38],[38,39],[22,39],[39,40],[40,41],[38,41],[20,41],[41,42],[37,42],[40,43],[42,43],[43,44],[41,44],[32,44],[38,44],[39,44],[43,45],[44,45],[44,46],[45,46],[45,47],[42,47],[43,48],[45,49],[45,50],[48,51],[30,51],[46,52],[48,52],[38,52],[51,52],[47,53],[45,53],[53,54],[48,54],[30,54],[50,55],[30,55],[36,55],[55,56],[39,56],[54,56],[50,57],[56,58],[32,58],[57,59],[49,59],[38,60],[60,61],[35,61],[54,61],[53,61],[54,62],[58,62],[62,63],[40,63],[58,63],[49,64],[63,64],[47,64],[39,64],[45,64],[62,65],[64,65],[54,65],[52,66],[61,66],[60,66],[55,67],[65,67],[45,68],[56,68],[36,68],[67,69],[66,69],[27,70],[60,70],[67,70],[48,71],[70,71],[53,71],[62,72],[72,73],[73,74]]))
    def test5(self):
        self.assertEqual(2,get_sol().largestPathValue("hhqhuqhqff",[[0,1],[0,2],[2,3]]))
    # def test6(self):
    # def test7(self):
    # def test8(self):

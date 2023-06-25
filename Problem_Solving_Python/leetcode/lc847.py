from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # bfs and (current_node, node_visited_mask) as state
    # (0->1->0) is same as (1->0). because in both cases:
    # 1. nodes visited are: [0,1]
    # 2. current_node: 0
    # https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/549233/Breadth-First-Search(BFS)with-intuitive-approach-Thinking-process-or-13-ms
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def turn_on(mask,i): return mask | (1<<i)
        def allSelected(mask, n): return mask == ((1 << n) - 1)

        n=len(graph)
        q = deque()
        for i in range(n):
            q.append([i,turn_on(0,i)]) # (node, visitMask)

        res=0
        vis=set()
        while q:
            for _ in range(len(q)):
                u,mask = q.popleft()
                if allSelected(mask,n): return res
                if (u,mask) in vis: continue
                vis.add((u,mask))
                for v in graph[u]:
                    newMask=turn_on(mask,v)
                    q.append([v,newMask])
            res+=1
class Solution4:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def all_node_visited(mask): return mask==2**n-1
        def turn_on(mask,i): return mask|(1<<i)
        n=len(graph)
        q=deque()
        for i in range(n):
            q.append((i,turn_on(0,i))) # to allow multiple visits to a node, we put all these simultaneously
        vis=set(q)
        res=0
        while q:
            for _ in range(len(q)):
                u,mask=q.popleft()
                if all_node_visited(mask):
                    return res
                for v in graph[u]:
                    new_state=(v,turn_on(mask,v))
                    if new_state not in vis:
                        q.append(new_state)
                        vis.add(new_state) # add next state so that other state in the current queue can't add the same state once again
            res+=1
class Solution2:
    # wrong
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def backtrack(u:int,nodes:set[int],edges:set[tuple]):
            if len(nodes)==n: return 0
            state = u,tuple(sorted(nodes)),tuple(sorted(edges))
            dp[state]=float('inf')
            for v in graph[u]:
                new_state=v,tuple(sorted(nodes.union({v}))),tuple(sorted(edges.union({(u,v)})))
                if new_state in dp: continue
                dp[state]=min(dp[state],1+backtrack(v,nodes.union({v}),edges.union({(u,v)})))
            return dp[state]


        n=len(graph)
        dp={}
        res=float('inf')
        for i in range(n):
            nodes={i}
            edges=set()
            res=min(res,backtrack(i,nodes,edges))
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().shortestPathLength(graph = [[1,2,3],[0],[0],[0]]))
    def test2(self):
        self.assertEqual(4,get_sol().shortestPathLength(graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]))
    def test3(self):
        self.assertEqual(5,get_sol().shortestPathLength(graph = [[1,2,3,4],[0,3],[0],[0,1],[0]]))
    def test4(self):
        self.assertEqual(11,get_sol().shortestPathLength(graph = [[2,3],[7],[0,6],[0,4,7],[3,8],[7],[2],[5,3,1],[4]]))
    def test5(self):
        self.assertEqual(11,get_sol().shortestPathLength(graph = [[2],[3],[0,4,5],[1,4],[2,3,6],[2],[4,7],[6,8],[7]]))
    def test6(self):
        self.assertEqual(9,get_sol().shortestPathLength(graph = [[2,3],[7],[0,8],[0,4,7],[3,6],[7],[2],[5,3,1],[4]]))
    def test7(self):
        self.assertEqual(13,get_sol().shortestPathLength(graph = [[2,5,7],[2,4],[0,1],[5],[5,6,1],[4,10,8,0,3],[4,9],[0],[5],[6],[5]]))
    def test8(self):
        self.assertEqual(14,get_sol().shortestPathLength(graph = [[2,3,5,7],[2,3,7],[0,1],[0,1],[7],[0],[10],[9,10,0,1,4],[9],[7,8],[7,6]]))
    def test9(self):
        self.assertEqual(11,get_sol().shortestPathLength(graph = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]))


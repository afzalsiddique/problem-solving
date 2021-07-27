import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bfs
    # https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339964/JavaPython-BFS
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        BIG=n*2 # max possible path len
        res=[[0,0]] + [[BIG,BIG] for _ in range(n-1)]
        g=[[[],[]] for _ in range(n)]
        for frm,to in red_edges: g[frm][0].append(to)
        for frm,to in blue_edges: g[frm][1].append(to)

        q=deque([[0,0],[0,1]])
        while q:
            for _ in range(len(q)):
                frm,c=q.popleft()
                for to in g[frm][c]:
                    if res[to][c]==BIG: # coming here for the first time
                        res[to][c]=res[frm][1-c]+1
                        q.append([to,1-c])

        new_res=[]
        for x,y in res:
            if x==BIG and y==BIG:
                new_res.append(-1)
            else:
                new_res.append(min(x,y))
        return new_res
class Solution2:
    # tle
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        MAX_PATH_LEN=n*2
        def find_shortest(to):
            if to==0: return 0
            q=deque([[0,0],[0,1]])
            cnt=-1
            while q:
                cnt+=1
                if cnt>MAX_PATH_LEN: return -1 # infinite circular path
                for _ in range(len(q)):
                    frm,c=q.popleft()
                    if frm==to: return cnt
                    for neigh in g[frm][c]:
                        q.append([neigh,1-c])
            return -1
        g=[[[],[]] for _ in range(n)]
        for frm,to in red_edges: g[frm][0].append(to)
        for frm,to in blue_edges: g[frm][1].append(to)

        res=[]
        for i in range(n):
            res.append(find_shortest(i))
        return res
class tester(unittest.TestCase):
    def test1(self):
        n = 3
        red_edges = [[0,1],[1,2]]
        blue_edges = []
        Output= [0,1,-1]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test2(self):
        n = 3
        red_edges = [[0,1]]
        blue_edges = [[2,1]]
        Output= [0,1,-1]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test3(self):
        n = 3
        red_edges = [[1,0]]
        blue_edges = [[2,1]]
        Output= [0,-1,-1]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test4(self):
        n = 3
        red_edges = [[0,1]]
        blue_edges = [[1,2]]
        Output= [0,1,2]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test5(self):
        n = 3
        red_edges = [[0,1],[0,2]]
        blue_edges = [[1,0]]
        Output= [0,1,1]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test6(self):
        n,red_edges,blue_edges = 5, [[2,0],[4,3],[4,4],[3,0],[1,4]], [[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]
        Output= [0, -1, -1, 1, -1]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test7(self):
        n,red_edges,blue_edges = 5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]
        Output= [0,1,2,3,7]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))
    def test8(self):
        n,red_edges,blue_edges = 100, [[95,4],[95,38],[56,93],[98,81],[22,76],[14,94],[14,28],[24,46],[35,64],[77,77],[57,51],[65,85],[83,97],[33,9],[16,49],[6,42],[73,84],[53,23],[63,49],[98,70],[85,98],[29,3],[87,16],[94,11],[19,61],[21,2],[73,48],[0,7],[42,5],[80,37],[27,25],[45,39],[52,87],[70,43],[95,97],[0,81],[5,41],[31,93],[92,23],[31,75],[99,56],[30,77],[18,33],[45,17],[83,12],[89,49],[17,22],[8,28],[45,87],[34,68],[41,91],[42,13],[3,40],[30,23],[16,2],[52,58],[19,17],[58,69],[64,61],[32,89],[91,1],[41,77],[47,19],[18,84],[99,36],[9,57],[86,61],[5,74],[57,99],[93,88],[0,15],[94,1],[15,34],[9,86],[24,1],[90,72],[1,72],[95,81],[58,59],[94,2],[19,52],[11,33],[8,22],[2,28],[39,5],[67,18],[33,77],[94,5],[54,37],[29,62],[60,6],[27,35],[6,96],[15,5],[13,31],[90,0],[91,45],[85,30],[29,29],[58,22],[90,87],[58,24],[8,33],[23,82],[96,51],[43,56],[68,59]], [[81,24],[98,66],[15,66],[78,20],[14,4],[39,10],[81,68],[61,0],[99,84],[76,82],[27,69],[97,80],[7,38],[77,13],[61,42],[1,6],[96,18],[74,28],[31,39],[3,86],[44,98],[85,45],[89,42],[23,55],[1,2],[1,40],[51,84],[14,45],[31,40],[33,20],[65,79],[41,85],[31,32],[81,55],[50,10],[53,24],[87,4],[8,15],[18,28],[73,18],[83,14],[35,26],[34,42],[59,81],[6,36],[13,42],[16,26],[54,16],[23,57],[9,50],[34,46],[46,27],[2,80],[14,83],[81,21],[19,48],[56,19],[53,35],[92,48],[85,18],[33,6],[37,17],[93,61],[63,1],[51,59],[40,22],[25,87],[99,73],[70,92],[87,54],[6,39],[54,81],[60,60],[41,54],[5,0],[31,46],[10,30],[1,98],[79,79],[6,49],[31,33],[62,15],[7,42],[19,3],[53,2],[69,74],[99,18],[86,65],[55,20],[3,58],[8,49],[52,13],[99,53],[29,70],[81,85],[9,82],[30,7],[69,44],[34,90],[41,18],[95,69],[5,59],[26,64],[21,37],[45,23],[60,37],[84,9],[92,49],[69,7],[77,28],[27,38],[94,66],[68,1],[29,22],[65,45],[19,43],[55,9],[92,0],[33,33],[70,87],[10,3],[21,28],[25,35],[51,2],[74,14],[79,1],[92,39],[12,41],[84,34],[91,77],[51,9],[87,73],[50,66],[2,19]]
        Output= [0, 3, 3, -1, 14, 3, 4, 1, -1, 8, 14, -1, -1, 3, -1, 1, 7, 5, 6, 4, 8, 2, 7, 7, 2, 5, 6, 4, 5, -1, 3, 7, 8, 7, 8, 5, -1, 5, 2, 8, 4, -1, 2, -1, -1, 12, 3, -1, 11, -1, 10, 9, 5, 10, 14, 2, -1, 8, -1, 3, -1, 5, -1, -1, 7, 10, 2, -1, 2, -1, 5, -1, 11, 10, -1, -1, -1, 9, -1, -1, 4, 1, 10, -1, 7, 2, 9, 6, -1, 9, -1, -1, 6, -1, -1, -1, 5, -1, 3, 9]
        self.assertEqual(Output,Solution().shortestAlternatingPaths(n,red_edges,blue_edges))

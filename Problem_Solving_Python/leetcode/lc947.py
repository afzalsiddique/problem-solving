import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution4()

class Solution:
    # dfs
    # https://www.youtube.com/watch?v=beOCN7G4h-M
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        vis=set()
        def dfs(i):
            if i in vis: return
            vis.add(i)
            for j in range(n):
                if i==j: continue
                if j in vis: continue
                x1,y1=stones[i][0],stones[i][1]
                x2,y2=stones[j][0],stones[j][1]
                if x1==x2: dfs(j)
                if y1==y2: dfs(j)
        no_of_islands=0
        for i in range(n):
            if i not in vis:
                dfs(i)
                no_of_islands+=1
        return n-no_of_islands
class Solution2:
    # dfs
    def removeStones(self, stones):
        def dfs(i, j):
            points.remove((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        points  = {(i, j) for i, j in stones}
        rows= defaultdict(list)
        cols = defaultdict(list)
        islands = 0
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                islands += 1
        return len(stones) - islands
class Solution3:
    # wrong dfs
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        # dp={}
        vis=set()
        def dfs(i):
            # if i in dp: return dp[i] # wrong
            vis.add(i)
            maxx=1
            for j in range(n):
                if i==j: continue
                if j in vis: continue
                x1,y1=stones[i][0],stones[i][1]
                x2,y2=stones[j][0],stones[j][1]
                if x1==x2:
                    maxx=max(maxx,1+dfs(j))
                if y1==y2:
                    maxx=max(maxx,1+dfs(j))
            vis.remove(i)
            # dp[i]=maxx
            return maxx
        maxx=1
        for i in range(n):
            maxx=max(maxx,dfs(i))
        return maxx-1

class Solution4:
    # union find
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        root = {}

        def add(x):
            if x not in root:
                root[x] = x

        def find(x):
            if x in root:
                p = root[x]
            else:
                p = x
            if p==x:
                return p

            root[x] = find(p)
            return root[x]

        def union(x,y):
            add(x),add(y)
            px,py = find(x), find(y)
            if px!=py:
                root[px] = py

        for row, col in stones:
            union('r'+str(row),'c'+str(col))

        unique_root_set = set()
        for temp_root in root.values():
            true_root = find(temp_root)
            unique_root_set.add(true_root)

        return n-len(unique_root_set)

class tester(unittest.TestCase):
    def test1(self):
        stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output= 5
        self.assertEqual(Output,Solution().removeStones(stones))
    def test2(self):
        stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output= 3
        self.assertEqual(Output,Solution().removeStones(stones))
    def test3(self):
        stones = [[0,0]]
        Output= 0
        self.assertEqual(Output,Solution().removeStones(stones))
    def test4(self):
        stones = [[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]
        Output= 10
        self.assertEqual(Output,Solution().removeStones(stones))
    def test5(self):
        stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
        Output= 4
        self.assertEqual(Output,Solution().removeStones(stones))

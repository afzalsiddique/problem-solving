from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def within(x:int,y:int)->bool:
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
            return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]
        def bfs(i,j,islandId):
            q=deque([(i,j)])
            res=0
            while q:
                i,j=q.popleft()
                if grid[i][j]==islandId:
                    continue
                grid[i][j]=islandId
                for x,y in get_4d_moves(i,j):
                    if grid[x][y]==1:
                        q.append((x,y))
                res+=1
            return res

        m,n=len(grid),len(grid[0])
        islandId=2
        islandSize=defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=1:
                    continue
                tmpSize=bfs(i,j,islandId)
                islandSize[islandId]=tmpSize
            islandId+=1

        maxx=max(islandSize.values() if islandSize else [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    continue
                res=0
                vis=set()
                for x,y in get_4d_moves(i,j):
                    islandId=grid[x][y]
                    if islandId in vis:
                        continue
                    vis.add(islandId)
                    res+=islandSize[islandId]
                maxx=max(maxx,res+1)
        return maxx

class Correct:
    # assign every cell an island_id where island_id>500
    # for every island_id store the size of that island in sizes
    # for every empty cell go in four directions and add the island_id to a set
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, vis): # return the size of the island
            if not 0<=i<n or not 0<=j<n: return 0
            if grid[i][j]==0: return 0
            if (i,j) in vis: return 0
            vis.add((i, j))
            ans=1
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ans += dfs(i + di, j + dj, vis)
            return ans

        n=len(grid)
        sizes=defaultdict(int)
        sizes[-1]=1
        island_id=501
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0: continue
                if grid[i][j]>500: continue # size already calculated
                vis=set()
                size=dfs(i,j,vis)
                for x,y in vis: grid[x][y]=island_id
                sizes[island_id]=size
                island_id+=1

        res=float('-inf')
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=0: continue
                sett=set()
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_i,new_j=i+di,j+dj
                    if not 0<=new_i<n or not 0<=new_j<n: continue
                    sett.add(grid[new_i][new_j])
                    ans=1
                    for island_id in sett:
                        ans+=sizes[island_id]
                    res=max(res,ans)


        # for x in grid: print(x)
        # print(sizes)
        res=max(res,max(sizes.values()))
        return res


class Tester(unittest.TestCase):
    def test01(self):
        grid=[[1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1],[1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1],[0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1],[0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1],[1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1],[1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0],[0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0],[1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1],[1,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1],[1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1],[1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0],[1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1],[1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0],[0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0],[0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1],[0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0],[0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1],[1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1],[1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1],[0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0],[0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0],[0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1],[0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1]]
        self.assertEqual(Correct().largestIsland(grid), Solution().largestIsland(grid))

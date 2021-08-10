import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # upscaled
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def dfs(i,j):
            if not 0<=i<m*3 or not 0<=j<n*3: return False
            if (i,j)==(m*3-2,n*3-2): return True # center of the bottom right cell
            if mat[i][j]==0: return False
            if (i,j) in vis: return False
            vis.add((i,j))
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if dfs(i+di,j+dj): return True
            vis.remove((i,j))
            return False

        # U=top middle; D=bottom middle; L=center left; R=center right; C=center
        U=(0,1); D=(2,1); L=(1,0); R=(1,2); C=(1,1)
        mapping={1:[L,C,R],2:[U,C,D],3:[L,C,D],4:[D,C,R],5:[L,C,U],6:[U,C,R]}
        m,n=len(grid),len(grid[0])
        mat=[[0]*(n*3) for _ in range(m*3)]
        vis=set()
        for old_i in range(m):
            for old_j in range(n):
                i=old_i*3
                j=old_j*3
                for di,dj in mapping[grid[old_i][old_j]]:
                    mat[i+di][j+dj]=1

        return dfs(1,1) # center of the top right cell
class Solution2:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def dfs(i,j,prev_di,prev_dj):
            if not 0<=i<m or not 0<=j<n: return False
            if (i,j) in vis: return False
            vis.add((i,j))
            if (-prev_di,-prev_dj)!=(INIT_di,INIT_dj) and (-prev_di,-prev_dj) not in turn[grid[i][j]]: # check if coming to this cell is valid
                return False
            if i==m-1 and j==n-1: return True
            for di,dj in turn[grid[i][j]]:
                if dfs(i+di,j+dj,di,dj): return True
            vis.remove((i,j))
            return False

        m,n=len(grid),len(grid[0])
        U=(-1,0); D=(1,0); L=(0,-1); R=(0,1)
        turn={1:[L,R],2:[U,D],3:[L,D],4:[R,D],5:[L,U],6:[U,R]}
        vis=set()
        INIT_di,INIT_dj = 0,0
        return dfs(0,0,INIT_di,INIT_dj)
class Solution3:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def dfs(i,j,pre_di,pre_dj):
            if not 0<=i<m or not 0<=j<n: return False
            if (-pre_di,-pre_dj) not in mat[i][j]: return False
            if (i,j) in vis: return False
            vis.add((i,j))
            if i==m-1 and j==n-1: return True
            for di,dj in mat[i][j]:
                if dfs(i+di,j+dj,di,dj):
                    return True
            vis.remove((i,j))
            return False
        L,R,U,D=[(0,-1),(0,1),(-1,0),(1,0)]
        vis=set()
        m,n=len(grid),len(grid[0])
        mat=[[set() for _ in range(n)] for __ in range(m)]
        mat[0][0].add((0,0)) # starting
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    mat[i][j].add(L)
                    mat[i][j].add(R)
                elif grid[i][j]==2:
                    mat[i][j].add(U)
                    mat[i][j].add(D)
                elif grid[i][j]==3:
                    mat[i][j].add(L)
                    mat[i][j].add(D)
                elif grid[i][j]==4:
                    mat[i][j].add(R)
                    mat[i][j].add(D)
                elif grid[i][j]==5:
                    mat[i][j].add(U)
                    mat[i][j].add(L)
                elif grid[i][j]==6:
                    mat[i][j].add(U)
                    mat[i][j].add(R)
        return dfs(0,0,0,0)



class Tester(unittest.TestCase):
    def test_1(self):
        grid = [[2,4,3],[6,5,2]]
        Output= True
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    def test_2(self):
        grid = [[1,2,1],[1,2,1]]
        Output= False
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    def test_3(self):
        grid = [[1,1,2]]
        Output= False
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    def test_4(self):
        grid = [[2],[2],[2],[2],[2],[2],[6]]
        Output= True
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    def test_5(self):
        grid = [[1,1,1,1,1,1,3]]
        Output= True
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    def test_6(self):
        grid = [[4,1],[6,1]]
        Output= True
        self.assertEqual(Output,get_sol().hasValidPath(grid))
    # def test_7(self):
    # def test_8(self):

import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        WALL1='\\'; WALL2='/'; PIPE=' '
        mm,nn=len(grid),len(grid[0])
        m,n=mm*3,nn*3
        mat=[[PIPE]*n for _ in range(m)]
        for ii in range(mm):
            for jj in range(nn):
                if grid[ii][jj]==1:
                    i,j=ii*3,jj*3
                    for _ in range(3):
                        mat[i][j]=WALL1
                        i+=1
                        j+=1
                else:
                    i,j=ii*3,jj*3+2
                    for _ in range(3):
                        mat[i][j]=WALL2
                        i+=1
                        j-=1
        for x in mat: print(''.join(x))

        def dfs(i,j,vis):
            if not 0<=j<n: return -1
            if i==m: return j
            if mat[i][j]==WALL1 or mat[i][j]==WALL2: return -1
            if (i,j) in vis: return -1
            vis.add((i, j))
            for di,dj in [(0,1),(0,-1),(1,0)]: # (left,right,down)
                ans=dfs(i+di,j+dj,vis)
                if ans!=-1:
                    return ans
            return ans

        res=[]
        for j in range(nn):
            col=j*3+1 # start from middle in the augmented mat
            ans=dfs(0,col,set())
            res.append(ans//3) # convert to original grid
        return res
class Solution2:
    # dp does not work better
    def findBall(self, grid: List[List[int]]) -> List[int]:
        WALL1='\\'; WALL2='/'; PIPE=' '
        mm,nn=len(grid),len(grid[0])
        m,n=mm*3,nn*3
        mat=[[PIPE]*n for _ in range(m)]
        for ii in range(mm):
            for jj in range(nn):
                if grid[ii][jj]==1:
                    i,j=ii*3,jj*3
                    for _ in range(3):
                        mat[i][j]=WALL1
                        i+=1
                        j+=1
                else:
                    i,j=ii*3,jj*3+2
                    for _ in range(3):
                        mat[i][j]=WALL2
                        i+=1
                        j-=1
        for x in mat: print(''.join(x))

        dp={}
        def dfs(i,j,vis):
            if (i,j) in dp: return dp[i,j]
            if not 0<=j<n: return -1
            if i==m: return j
            if mat[i][j]==WALL1 or mat[i][j]==WALL2: return -1
            if (i,j) in vis: return -1
            vis.add((i, j))
            for di,dj in [(0,1),(0,-1),(1,0)]: # (left,right,down)
                ans=dfs(i+di,j+dj,vis)
                if ans!=-1:
                    dp[i,j]=ans
                    return ans
            dp[i,j]=ans
            return ans

        res=[]
        for j in range(nn):
            col=j*3+1 # start from middle in the augmented mat
            ans=dfs(0,col,set())
            res.append(ans//3) # convert to original grid
        return res
class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
        Output= [1,-1,-1,-1,-1]
        self.assertEqual(Output, get_sol().findBall(grid))
    def test_2(self):
        grid = [[-1]]
        Output= [-1]
        self.assertEqual(Output, get_sol().findBall(grid))
    def test_3(self):
        grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
        Output= [0,1,2,3,4,-1]
        self.assertEqual(Output, get_sol().findBall(grid))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
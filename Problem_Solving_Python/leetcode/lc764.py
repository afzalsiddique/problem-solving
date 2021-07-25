import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/largest-plus-sign/discuss/113314/JavaC++Python-O(N2)-solution-using-only-one-grid-matrix/114381
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for i in range(n)]
        for m in mines: grid[m[0]][m[1]] = 0

        for i in range(n):
            cnt=0
            for j in range(n): # how far left it can reach.
                if grid[i][j]: cnt+=1
                else: cnt=0
                grid[i][j]=cnt

        for i in range(n):
            cnt=0
            for j in reversed(range(n)): # how far right it can reach.
                if grid[i][j]: cnt+=1
                else: cnt=0
                grid[i][j]=min(grid[i][j],cnt)

        for j in range(n):
            cnt=0
            for i in range(n): # how far up it can reach.
                if grid[i][j]: cnt+=1
                else: cnt=0
                grid[i][j]=min(grid[i][j],cnt)

        for j in range(n):
            cnt=0
            for i in reversed(range(n)): # how down right it can reach.
                if grid[i][j]: cnt+=1
                else: cnt=0
                grid[i][j]=min(grid[i][j],cnt)

        # for x in grid: print(x)
        res=0
        for i in range(n):
            for j in range(n):
                res=max(res,grid[i][j])
        return res
class Solution2:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # if n==1: return 0
        if len(mines)==n*n: return 0
        mines = set(map(tuple,mines))
        grid=[[1]*n for _ in range(n)]
        for i,j in mines: grid[i][j]=0
        up=[[0]*n for _ in range(n)]
        down=[[0]*n for _ in range(n)]
        left=[[0]*n for _ in range(n)]
        right=[[0]*n for _ in range(n)]
        res=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0: continue
                if j==0 or j>0 and right[i][j-1]==0:
                    cnt=0
                    k=j+1
                    while k<n and grid[i][k]==1:
                        cnt+=1
                        k+=1
                    right[i][j]=cnt
                else:
                    right[i][j]=right[i][j-1]-1
        for i in range(n):
            for j in range(n-1,-1,-1):
                if grid[i][j]==0: continue
                if j==n-1 or j<n-1 and left[i][j+1]==0:
                    cnt=0
                    k=j-1
                    while k>=0 and grid[i][k]==1:
                        cnt+=1
                        k-=1
                    left[i][j]=cnt
                else:
                    left[i][j]=left[i][j+1]-1
        for j in range(n):
            for i in range(n):
                if grid[i][j]==0: continue
                if i==0 or i>0 and down[i-1][j]==0:
                    cnt=0
                    k=i+1
                    while k<n and grid[k][j]==1:
                        cnt+=1
                        k+=1
                    down[i][j]=cnt
                else:
                    down[i][j]=down[i-1][j]-1
        for j in range(n):
            for i in range(n-1,-1,-1):
                if grid[i][j]==0: continue
                if i==n-1 or i<n-1 and up[i+1][j]==0:
                    cnt=0
                    k=i-1
                    while k>=0 and grid[k][j]==1:
                        cnt+=1
                        k-=1
                    up[i][j]=cnt
                else:
                    up[i][j]=up[i+1][j]-1
        maxx=0
        for i in range(n):
            for j in range(n):
                res[i][j]=min(left[i][j],right[i][j],down[i][j],up[i][j])
                maxx=max(maxx,res[i][j])
        # for x in res: print(x)
        return maxx+1
class tester(unittest.TestCase):
    def test_1(self):
        n,mines,Output = 5, [[4,2]], 2
        self.assertEqual(Output, get_sol().orderOfLargestPlusSign(n,mines))
    def test_2(self):
        n,mines,Output = 1, [[0,0]], 0
        self.assertEqual(Output, get_sol().orderOfLargestPlusSign(n,mines))
    def test_3(self):
        n,mines,Output = 2, [[0,0],[0,1],[1,0]],1
        self.assertEqual(Output, get_sol().orderOfLargestPlusSign(n,mines))
    def test_4(self):
        n,mines,Output = 2, [[0,0],[0,1],[1,0],[1,1]],0
        self.assertEqual(Output, get_sol().orderOfLargestPlusSign(n,mines))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # work both ways top-left to bottom-right and bottom-right to top-left
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD=10**9+7

        def h(i, j):
            """Return maximum & minimum products ending at (i, j)."""
            if (i,j) in dp_min: return dp_min[i,j],dp_max[i,j]
            if i==m or j==n: return float('-inf'), float('inf')
            if (i,j)==(m-1,n-1): return grid[m-1][n-1], grid[m-1][n-1]
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = h(i+1, j) # from down
            mx2, mn2 = h(i, j+1) # from right
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            dp_min[i,j],dp_max[i,j] = (mx,mn) if grid[i][j]>0 else (mn,mx)
            return dp_min[i,j],dp_max[i,j]

        dp_max={}
        dp_min={}
        mx, _ = h(0, 0)
        return -1 if mx < 0 else mx % MOD
class Solution2:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9+7

        def h(i, j):
            """Return maximum & minimum products ending at (i, j)."""
            if (i,j) in dp_min: return dp_min[i,j],dp_max[i,j]
            if i == 0 and j == 0: return grid[0][0], grid[0][0]
            if i < 0 or j < 0: return float('-inf'), float('inf')
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = h(i-1, j) # from top
            mx2, mn2 = h(i, j-1) # from left
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            dp_min[i,j],dp_max[i,j] = (mx,mn) if grid[i][j]>0 else (mn,mx)
            return dp_min[i,j],dp_max[i,j]

        dp_max={}
        dp_min={}
        mx, _ = h(m-1, n-1)
        return -1 if mx < 0 else mx % MOD
class Solution3:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def h(i,j):
            """Return maximum & minimum products ending at (i, j)."""
            if not 0<=i<m or not 0<=j<n: return float('-inf'),float('inf')
            if (i,j) in dp_max: return dp_max[i,j], dp_min[i,j]
            if (i,j)==(m-1,n-1):
                if grid[i][j]>0:
                    dp_max[i,j]=grid[i][j]
                    dp_min[i,j]=float('inf')
                elif grid[i][j]<0:
                    dp_min[i,j]=grid[i][j]
                    dp_max[i,j]=float('-inf')
                else:
                    dp_max[i,j]=0
                    dp_min[i,j]=0
                return dp_max[i,j],dp_min[i,j]
            for di,dj in [(1,0),(0,1)]:
                ans_pos,ans_neg=h(i+di,j+dj)
                if grid[i][j]>0:
                    dp_max[i,j]=max(dp_max[i,j],ans_pos*grid[i][j])
                    dp_min[i,j]=min(dp_min[i,j],ans_neg*grid[i][j])
                elif grid[i][j]<0:
                    dp_max[i,j]=max(dp_max[i,j],ans_neg*grid[i][j])
                    dp_min[i,j]=min(dp_min[i,j],ans_pos*grid[i][j])
                else:
                    dp_max[i,j]=max(dp_max[i,j],0)
                    dp_min[i,j]=min(dp_min[i,j],0)
            return dp_max[i,j],dp_min[i,j]

        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        dp_max=defaultdict(lambda:float('-inf'))
        dp_min=defaultdict(lambda:float('inf'))
        h(0,0)
        # print(dp_max)
        # print(dp_min)
        ans=dp_max[0,0]
        return ans%MOD if ans>=0 else -1

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[-1,-2,-3], [-2,-3,-3], [-3,-3,-2]]
        Output= -1
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_2(self):
        grid = [[1,-2,1], [1,-2,1], [3,-4,1]]
        Output= 8
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_3(self):
        grid = [[1, 3], [0,-4]]
        Output= 0
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_4(self):
        grid = [[ 1, 4,4,0], [-2, 0,0,1], [ 1,-1,1,1]]
        Output= 2
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_5(self):
        grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
        Output= -1
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_6(self):
        grid = [[1,3],[0,-4]]
        Output= 0
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_7(self):
        grid = [[-1,1,-2,-1],[3,-3,-2,0]]
        Output= 0
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_8(self):
        grid = [[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]]
        Output= 19215865
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    # def test_9(self):
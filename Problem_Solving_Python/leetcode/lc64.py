from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n:
                return float('inf')
            if x==m-1 and y==n-1: return grid[x][y]
            res=float('inf')
            for dx,dy in [(0,1),(1,0)]:
                res=min(res,grid[x][y]+dfs(x+dx,y+dy))
            return res

        m,n=len(grid),len(grid[0])
        return dfs(0,0)
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        for row in range(1, m):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
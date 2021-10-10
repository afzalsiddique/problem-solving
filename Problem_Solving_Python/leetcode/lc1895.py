import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        presum_row = [[0]*n for _ in range(m)]
        presum_col = [[0]*n for _ in range(m)]
        presum_diag1 = [[0]*n for _ in range(m)]
        presum_diag2 = [[0]*n for _ in range(m)]


        for i in range(m):
            cur = 0
            for j in range(n):
                cur += grid[i][j]
                presum_row[i][j]=cur

        for j in range(n):
            cur = 0
            for i in range(m):
                cur += grid[i][j]
                presum_col[i][j]=cur

        for i in range(m):
            cur = 0
            row,col = i,0
            while row<m and col<n:
                cur += grid[row][col]
                presum_diag1[row][col]= cur
                row+=1; col+=1

        for j in range(1,n):
            cur = 0
            row,col = 0,j
            while row<m and col<n:
                cur += grid[row][col]
                presum_diag1[row][col]= cur
                row+=1; col+=1

        for i in range(m):
            curr = 0
            r,c = i,n-1
            while r<m and c>=0:
                curr += grid[r][c]
                presum_diag2[r][c]= curr
                r+=1; c-=1
        for j in range(1,n):
            currr = 0
            rr,cc = 0,n-1-j
            while rr<m and cc>=0:
                currr += grid[rr][cc]
                presum_diag2[rr][cc]= currr
                rr+=1; cc-=1

        def check(x1, y1, size):
            x2 = x1 + size - 1
            y2 = y1 + size - 1
            if not 0<=x2<m or not 0<=y2<n: return False
            val = presum_row[x1][y2] - presum_row[x1][y1] + grid[x1][y1]
            for x in range(x1,x2+1):
                tmp = presum_row[x][y2] - presum_row[x][y1] + grid[x][y1]
                if tmp!=val: return False
            for y in range(y1,y2+1):
                tmp = presum_col[x2][y] - presum_col[x1][y] + grid[x1][y]
                if tmp!=val: return False
            tmp = presum_diag1[x2][y2]-presum_diag1[x1][y1]+grid[x1][y1]
            if tmp != val: return False
            tmp = presum_diag2[x2][y1]-presum_diag2[x1][y2]+grid[x1][y2]
            if tmp!= val: return False
            return True

        maxx = 1
        for i in range(m):
            for j in range(n):
                for size in range(2,max(m,n)+1):
                    if check(i,j,size):
                        maxx=max(maxx,size)
        return maxx



class MyTestCase(unittest.TestCase):
    def test1(self):
        grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
        Output= 3
        self.assertEqual(Output, get_sol().largestMagicSquare(grid))
    def test2(self):
        grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
        Output= 2
        self.assertEqual(Output, get_sol().largestMagicSquare(grid))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):

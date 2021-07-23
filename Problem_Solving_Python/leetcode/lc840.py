import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def valid(r, c): # start_row,start_col
            sett=set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if not 1<=grid[i][j]<=9: return False
                    if grid[i][j] in sett: return False
                    sett.add(grid[i][j])
            summ = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
            summ = 15 # works because 1+2+3..+8+9=45. distribute it into 3 rows. Each row gets 15
            if any(sum(grid[r+i][j] for j in range(c, c + 3)) != summ for i in range(3)): return False # rows check
            if any(sum(grid[i][c+j] for i in range(r, r + 3)) != summ for j in range(3)): return False # cols check
            if sum(grid[r + i][c + i] for i in range(3)) != summ: return False # diag1
            if sum(grid[r + i][c + 2 - i] for i in range(3)) != summ: return False # diag2
            return True

        m,n=len(grid),len(grid[0])
        if m<3 or n<3: return 0
        cnt=0
        for r1 in range(m-3+1):
            for c1 in range(n-3+1):
                if valid(r1,c1):
                    cnt+=1
        return cnt
class Solution2:
    # wrong
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def valid(r, c): # start_row,start_col
            summ = 15 # this case will fail. grid = [[5,5,5],[5,5,5],[5,5,5]]
            if any(sum(grid[r+i][j] for j in range(c, c + 3)) != summ for i in range(3)): return False # rows check
            if any(sum(grid[i][c+j] for i in range(r, r + 3)) != summ for j in range(3)): return False # cols check
            if sum(grid[r + i][c + i] for i in range(3)) != summ: return False # diag1
            if sum(grid[r + i][c + 2 - i] for i in range(3)) != summ: return False # diag2
            return True

        m,n=len(grid),len(grid[0])
        if m<3 or n<3: return 0
        cnt=0
        for r1 in range(m-3+1):
            for c1 in range(n-3+1):
                if valid(r1,c1):
                    cnt+=1
        return cnt

class tester(unittest.TestCase):
    def test_1(self):
        grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        Output= 1
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_2(self):
        grid = [[8]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_3(self):
        grid = [[4,4],[3,3]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_4(self):
        grid = [[4,7,8],[9,5,1],[2,3,6]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_5(self):
        grid = [[10,3,5],[1,6,11],[7,9,2]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_6(self):
        grid = [[7,0,5],[2,4,6],[3,8,1]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    def test_7(self):
        grid = [[5,5,5],[5,5,5],[5,5,5]]
        Output= 0
        self.assertEqual(Output,get_sol().numMagicSquaresInside(grid))
    # def test_8(self):

from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len((board[0]))

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:return
            if board[i][j]!='O':return
            board[i][j]='s'
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x,y=i+dx,j+dy
                dfs(x,y)
        # "Save" every O-region touching the border, changing its cells to 's'.
        for i in [0,m-1]: # first row and last row
            for j in range(n):
                dfs(i,j)

        for i in range(m): # first col and last col
            for j in [0,n-1]:
                dfs(i,j)
        # Change every 's' on the board to 'O' and everything else to 'X'.
        for i in range(m):
            for j in range(n):
                if board[i][j]!='s':
                    board[i][j]='X'
                else:
                    board[i][j]='O'

class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        if m==0:
            return
        n = len(board[0])
        boolean = [[True]*n for _ in range(m)]

        def traverse(row, col):
            if row < 0 or row >= m:
                return
            if col < 0 or col >= n:
                return
            # [["O","O"],["O","O"]] for this case boolean[row][col] is necessary
            if board[row][col] == 'O' and boolean[row][col]:
                boolean[row][col] = False
                traverse(row, col+1)
                traverse(row, col-1)
                traverse(row+1, col)
                traverse(row-1, col)

        # find where it can't be flipped
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    if board[i][j] == 'O':
                        traverse(i, j)
            else:
                if board[i][0] == 'O':
                    traverse(i, 0)
                if board[i][-1] == 'O':
                    traverse(i, n-1)

        # flip
        for i in range(m):
            for j in range(n):
                if boolean[i][j]:
                    board[i][j] = 'X'

class MyTestCase(unittest.TestCase):
    def test01(self):
        board = [["X", "X", "X", "X"],
                 ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"],
                 ["X", "O", "X", "X"],
                 ]
        expected = [["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"],
                    ]
        get_sol().solve(board)
        self.assertEqual(expected, board)
    def test02(self):
        board = [["O","O"],["O","O"]]
        expected = [["O","O"],["O","O"]]
        get_sol().solve(board)
        self.assertEqual(expected, board)
    def test03(self):
        board = [["X", "X", "X", "X"],
                 ["O", "O", "O", "O"],
                 ["X", "X", "O", "X"],
                 ["X", "X", "X", "X"],
                 ]
        expected = [["X", "X", "X", "X"],
                    ["O", "O", "O", "O"],
                    ["X", "X", "O", "X"],
                    ["X", "X", "X", "X"],
                    ]
        get_sol().solve(board)
        self.assertEqual(expected, board)
    def test04(self):
        board = [["O"]]
        expected = [["O"]]
        get_sol().solve(board)
        self.assertEqual(expected, board)
    def test05(self):
        board = [["O","O"]]
        expected = [["O","O"]]
        get_sol().solve(board)
        self.assertEqual(expected, board)
    def test06(self):
        board = [["O","X"]]
        expected = [["O","X"]]
        get_sol().solve(board)
        self.assertEqual(expected, board)

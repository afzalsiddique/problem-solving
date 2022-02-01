from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=xFv_Hl4B83A&t=529s
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def diag1Key(row,col): return row-col
        def diag2Key(row,col): return row+col
        def possible(row,col):
            if col in queens: return False
            if diag1Key(row,col) in diag1: return False
            if diag2Key(row,col) in diag2: return False
            return True
        def backtrack(row):
            if row==n:
                res.append(queens[:])
                return
            for col in range(n):
                if possible(row,col):
                    queens[row]=col
                    diag1.add(diag1Key(row,col))
                    diag2.add(diag2Key(row,col))
                    backtrack(row+1)
                    queens[row]=-1
                    diag1.remove(diag1Key(row,col))
                    diag2.remove(diag2Key(row,col))
        def createBoard(queens):
            board=[['.' for _ in range(n)] for _ in range(n)]
            for row,col in enumerate(queens):
                board[row][col]='Q'
            return list(map(''.join,board))
        def createAllBoards():
            return [createBoard(queens) for queens in res]

        queens=[-1]*n
        diag1=set()
        diag2=set()
        res=[]
        backtrack(0)
        return createAllBoards()
class Solution4:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n
        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        # index represents row no and value represents col no

        def place_queen(ith_row): # dfs
            if ith_row == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for col_no in range(len(queens)):
                queens[ith_row] = col_no
                if valid(ith_row):  # pruning
                    place_queen(ith_row + 1)
                queens[ith_row] = -1

        # check whether queen can be placed in nth row
        def valid(nth_row):
            for i in range(nth_row):
                if abs(queens[i] - queens[nth_row]) == nth_row - i:  # same digonal
                    return False
                if queens[i] == queens[nth_row]:  # same column
                    return False
            return True


        # given queens = [1,3,0,2] this function returns
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] = 'Q'
            for row in board_temp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards

        place_queen(0)
        return make_all_boards(res)


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1]*n
        res = []
        def valid(row,col):
            for i in range(n):
                if queens[i]==-1:break
                if col==queens[i]:return False
                if abs(row-i)==abs(col-queens[i]):return False
            return True
        def dfs(ith_row):
            if ith_row==n:
                res.append(queens[:])
                return
            for col in range(n):
                if valid(ith_row, col):
                    queens[ith_row]=col
                    dfs(ith_row + 1)
                    queens[ith_row]=-1

        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] = 'Q'
            for row in board_temp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards

        dfs(0)
        return make_all_boards(res)

class Solution3:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def colCheck():
            return len(set(queens))==len(queens)
        def diag1Check():
            diag1=defaultdict(int)
            for i,j in enumerate(queens):
                if diag1[j-i]==1:
                    return False
                diag1[j-i]+=1
            return True
        def diag2Check():
            diag2=defaultdict(int)
            for i,j in enumerate(queens):
                if diag2[i+j]==1:
                    return False
                diag2[i+j]+=1
            return True

        def backtrack(i: int):
            if i==n:
                res.append(queens[:])
                return
            for j in range(n):
                queens.append(j)
                if colCheck() and diag1Check() and diag2Check():
                    backtrack(i + 1)
                queens.pop()
        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] = 'Q'
            for row in board_temp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards

        res=[]
        queens=[]
        backtrack(0)
        res=make_all_boards(res)
        return res
class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual = sorted(get_sol().solveNQueens(4))
        expected = sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
        self.assertEqual(expected, actual)

    def test_2(self):
        actual = sorted(get_sol().solveNQueens(5))
        expected = sorted([['....Q', '..Q..', 'Q....', '...Q.', '.Q...'],
                         ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'],
                         ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
                         ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'],
                         ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
                         ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'],
                         ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
                         ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'],
                         ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
                         ['Q....', '..Q..', '....Q', '.Q...', '...Q.']] )
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = sorted(get_sol().solveNQueens(3))
        expected = sorted([])
        self.assertEqual(expected, actual)
    def test_4(self):
        actual = sorted(get_sol().solveNQueens(2))
        expected = sorted([])
        self.assertEqual(expected, actual)
    def test_5(self):
        actual = sorted(get_sol().solveNQueens(1))
        expected = sorted([['Q']])
        self.assertEqual(expected, actual)






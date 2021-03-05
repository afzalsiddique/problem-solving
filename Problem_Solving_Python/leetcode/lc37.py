# https://leetcode.com/problems/sudoku-solver/discuss/15959/Accepted-Python-solution
import unittest
from typing import List


class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True

        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True # if placing this number solves sudoku in future then return
                self.board[row][col] = '.' # otherwise remove this number

    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe

    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        sol.solveSudoku(board)
        expected = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        self.assertEqual(expected, board)
    def test_2(self):
        sol = Solution()
        board = [["5","3",".",".","7",".",".",".","."],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        sol.solveSudoku(board)
        expected = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        self.assertEqual(expected, board)
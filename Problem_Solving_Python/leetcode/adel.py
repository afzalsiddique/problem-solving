import unittest
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check_row(row, value):
            r = board[row]
            if value in r:return False
            return True

        def check_col(col, value):
            column = [row[col] for row in board]
            if value in column: return False
            return True

        def check_subgrid(row, col, value):
            subgrid_row = row // 3
            subgrid_col = col // 3
            start_row = subgrid_row * 3
            end_row = (subgrid_row + 1) * 3
            start_col = subgrid_col * 3
            end_col = (subgrid_col + 1) * 3
            for i in range(start_row, end_row):
                for j in range(start_col, end_col):
                    if board[row][col] == value: return False
            return True


        def findUnassigned():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        return row, col
            return -1, -1

        def valid(row, col, value):
            return check_row(row, value) and check_col(col, value) and check_subgrid(row, col, value)

        def place_value(row, col):
            if row==9 and col==9:
                return
            for value in range(1,9+1):
                if valid(row,col, str(value)):
                    board[row][col]=str(value)
                    next_row, next_col = findUnassigned()
                    if next_row==9 and next_col==9:return
                    place_value(next_row, next_col)
        next_row, next_col = findUnassigned()
        place_value(next_row, next_col)




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

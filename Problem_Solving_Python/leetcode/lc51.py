# https://leetcode.com/problems/n-queens/
# https://www.youtube.com/watch?v=xFv_Hl4B83A&t=529s
import unittest
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n
        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        # index represents row no and value represents col no

        def place_queen(nth_row): # dfs
            if nth_row == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for col_no in range(len(queens)):
                queens[nth_row] = col_no
                if valid(nth_row):  # pruning
                    place_queen(nth_row + 1)
                queens[nth_row] = -1

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



class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(4))
        expected = sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(5))
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
        solution = Solution()
        actual = sorted(solution.solveNQueens(3))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(2))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(1))
        expected = sorted([['Q']])
        self.assertEqual(expected, actual)






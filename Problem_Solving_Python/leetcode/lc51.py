# https://leetcode.com/problems/n-queens/
# https://www.youtube.com/watch?v=xFv_Hl4B83A&t=529s
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

        def dfs(index):
            if index == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):  # pruning
                    dfs(index + 1, )

        # check whether nth queens can be placed
        def valid(n):
            for i in range(n):
                if abs(queens[i] - queens[n]) == n - i:  # same digonal
                    return False
                if queens[i] == queens[n]:  # same column
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

        dfs(0)
        return make_all_boards(res)







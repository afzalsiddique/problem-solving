# https://leetcode.com/problems/surrounded-regions/
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
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


# https://leetcode.com/problems/surrounded-regions/
from typing import List


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
        # "Save" every O-region touching the border, changing its cells to 'S'.
        for i in [0,m-1]: # first row and last row
            for j in range(n):
                dfs(i,j)

        for i in range(m): # first col and last col
            for j in [0,n-1]:
                dfs(i,j)
        # Change every 'S' on the board to 'O' and everything else to 'X'.
        for i in range(m):
            for j in range(n):
                if board[i][j]!='s':
                    board[i][j]='X'
                else:
                    board[i][j]='O'

    def solve2(self, board: List[List[str]]) -> None:
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


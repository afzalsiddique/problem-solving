# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        selected = [[False] * n for _ in range(m)]

        def backtrack(idx, i, j):
            if idx == len(word):
                return True
            if board[i][j] == word[idx] and not selected[i][j]:
                selected[i][j] = True
                if i + 1 < m and backtrack(idx + 1, i + 1, j):
                    return True
                if i - 1 > -1 and backtrack(idx + 1, i - 1, j):
                    return True
                if j + 1 < n and backtrack(idx + 1, i, j + 1):
                    return True
                if j - 1 > -1 and backtrack(idx + 1, i, j - 1):
                    return True
                selected[i][j] = False
            return False

        if len(word) > m * n: # for this case -> board = [["a"]], word = "ab"
            return False
        if m == 1 and n == 1: # for this case -> board = [["A"]], word = "A"
            return True if board[0][0] == word[0][0] else False

        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j):
                    return True
        return False

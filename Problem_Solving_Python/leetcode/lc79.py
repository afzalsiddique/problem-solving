from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def exist(self, mat: List[List[str]], word: str) -> bool:
        def recur(i,x,y):
            if i==len(word): return True
            if not 0<=x<m or not 0<=y<n: return False
            if mat[x][y]!=word[i]: return False

            letter=mat[x][y]
            mat[x][y]='#'
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                if recur(i+1,x+dx,y+dy):
                    return True
            mat[x][y]=letter
            return False


        m,n= len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if recur(0,i,j):
                    return True
        return False
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        selected = [[False] * n for _ in range(m)]

        def backtrack(idx, x, y):
            if idx == len(word):
                return True
            if not 0<=x<m or not 0<=y<n:
                return False
            if board[x][y] == word[idx] and not selected[x][y]:
                selected[x][y] = True
                if backtrack(idx + 1, x + 1, y):
                    return True
                if backtrack(idx + 1, x - 1, y):
                    return True
                if backtrack(idx + 1, x, y + 1):
                    return True
                if backtrack(idx + 1, x, y - 1):
                    return True
                selected[x][y] = False
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
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,get_sol().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    def test02(self):
        self.assertEqual(True,get_sol().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    def test03(self):
        self.assertEqual(False,get_sol().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
    def test04(self):
        self.assertEqual(False,get_sol().exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB"))
    def test05(self):
        self.assertEqual(True,get_sol().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

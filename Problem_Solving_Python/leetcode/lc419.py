import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
# without modifying the board
# time O(m*n) space O(1)
class Solution:
    # https://www.youtube.com/watch?v=wBG6078g1gE
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n=len(board),len(board[0])
        cnt=0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.': continue
                if i>0 and board[i-1][j]=='X': continue
                if j>0 and board[i][j-1]=='X': continue
                cnt+=1
        return cnt

# modifies the board
# time O(m*n) space O(max(m,n))
class Solution2:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n=len(board),len(board[0])
        dirs = [(1,0),(0,1)]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n: return
            if board[i][j]=='.': return
            board[i][j]='.'
            for di,dj in dirs:
                new_i,new_j = i+di,j+dj
                dfs(new_i,new_j)

        cnt=0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    dfs(i,j)
                    cnt+=1
        return cnt

class tester(unittest.TestCase):
    def test1(self):
        board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        Output= 2
        self.assertEqual(Output,Solution().countBattleships(board))
    def test2(self):
        board = [["."]]
        Output= 0
        self.assertEqual(Output,Solution().countBattleships(board))
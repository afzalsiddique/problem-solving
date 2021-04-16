import builtins
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List




# https://www.youtube.com/watch?v=aXAuZ6oGano
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n=len(board),len(board[0])
        LIVE,DEAD,LIVE_to_DEAD,DEAD_to_LIVE=1,0,2,3

        def valid(i,j):
            if i>=m or j>=n or i<0 or j<0: return False
            return True

        def get_state(i, j):
            cnt=0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                x,y=i+dx,j+dy
                if valid(x,y):
                    if board[x][y]==LIVE or board[x][y]==LIVE_to_DEAD:
                        cnt+=1
            if board[i][j]==LIVE or board[i][j]==LIVE_to_DEAD:
                if cnt<2 or cnt>3:
                    return LIVE_to_DEAD
                return LIVE
            elif board[i][j]==DEAD or board[i][j]==DEAD_to_LIVE:
                if cnt==3:
                    return DEAD_to_LIVE
                return DEAD

        for i in range(m):
            for j in range(n):
                state=get_state(i,j)
                board[i][j]=state

        for i in range(m):
            for j in range(n):
                if board[i][j]==LIVE_to_DEAD:
                    board[i][j]=DEAD
                elif board[i][j]==DEAD_to_LIVE:
                    board[i][j]=LIVE

class tester(unittest.TestCase):
    def test1(self):
        board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Solution().gameOfLife(board)
        self.assertEqual([[0,0,0],[1,0,1],[0,1,1],[0,1,0]],board)
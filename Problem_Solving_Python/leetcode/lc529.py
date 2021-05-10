import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()



class Solution:
    # https://www.youtube.com/watch?v=lla6QlAF4HQ
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m,n=len(board),len(board[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        vis=set()
        def get_no_bombs(i,j):
            bombs_adjacent=0
            for di,dj in dir:
                x,y=i+di,j+dj
                if 0<=x<m and 0<=y<n and board[x][y]=='M':
                    bombs_adjacent+=1
            return bombs_adjacent
        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0: return
            if board[i][j]=='M': return
            if (i,j) in vis: return
            vis.add((i,j))
            bombs_adjacent = get_no_bombs(i,j)
            if bombs_adjacent==0:
                board[i][j]='B'
                for di,dj in dir:
                    dfs(i+di,j+dj)
            else:
                board[i][j]=str(bombs_adjacent)


        i,j=click[0],click[1]
        if board[i][j]=='M':
            board[i][j]='X'
            return board
        dfs(i,j)
        return board

class tester(unittest.TestCase):
    def test1(self):
        board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
        click = [3,0]
        Output= [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        self.assertEqual(Output,Solution().updateBoard(board,click))
    def test2(self):
        board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        click = [1,2]
        Output= [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        self.assertEqual(Output,Solution().updateBoard(board,click))


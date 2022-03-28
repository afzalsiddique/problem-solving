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
        def get_no_bombs(x,y):
            return sum(1 for dx,dy in dirs if 0<=x+dx<m and 0<=y+dy<n and board[x+dx][y+dy]=='M')
        def dfs(x, y):
            if x>=m or y>=n or x<0 or y<0: return
            if board[x][y]== 'M': return
            if (x, y) in vis: return
            vis.add((x, y))
            bombs_adjacent = get_no_bombs(x, y)
            if bombs_adjacent==0:
                board[x][y]= 'B'
                for dx,dy in dirs:
                    dfs(x + dx, y + dy)
            else:
                board[x][y]=str(bombs_adjacent)


        m,n=len(board),len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        vis=set()
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
        self.assertEqual(Output,get_sol().updateBoard(board,click))
    def test2(self):
        board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        click = [1,2]
        Output= [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        self.assertEqual(Output,get_sol().updateBoard(board,click))


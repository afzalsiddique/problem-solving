from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def gameOfLife(self, mat: List[List[int]]) -> None:
        LIVE,LIVE_TO_DEAD,LIVE_TO_LIVE=1,3,5 # all odd. LIVE_TO_something
        DEAD,DEAD_TO_DEAD,DEAD_TO_LIVE=0,2,4 # all even. DEAD_TO_something
        # also possible with these
        # LIVE,LIVE_TO_DEAD=1,3 # all odd. LIVE_TO_something
        # DEAD,DEAD_TO_LIVE=0,2 # all even. DEAD_TO_something
        def wasAlive(x,y): return mat[x][y]%2==1
        def nextState(x,y):
            liveNeighbours=0
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                X,Y=x+dx,y+dy
                if 0<=X<m and 0<=Y<n: liveNeighbours+=wasAlive(X,Y)
            if wasAlive(x,y):
                if liveNeighbours<2 or liveNeighbours>3:
                    return LIVE_TO_DEAD
                return LIVE_TO_LIVE
            else: # was dead
                if liveNeighbours==3:
                    return DEAD_TO_LIVE
                return DEAD_TO_DEAD


        m,n= len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                mat[i][j]=nextState(i,j)

        for i in range(m):
            for j in range(n):
                if mat[i][j] in [LIVE_TO_LIVE,DEAD_TO_LIVE]: # something_TO_LIVE
                    mat[i][j]=LIVE
                else: # elif mat[i][j] in [DEAD_TO_DEAD,LIVE_TO_DEAD] # something_TO_DEAD
                    mat[i][j]=DEAD
class Solution2:
    # https://www.youtube.com/watch?v=aXAuZ6oGano
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

class Tester(unittest.TestCase):
    def test01(self):
        board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        get_sol().gameOfLife(board)
        self.assertEqual([[0,0,0],[1,0,1],[0,1,1],[0,1,0]],board)
    def test02(self):
        board=[[1,1],[1,0]]
        get_sol().gameOfLife(board)
        self.assertEqual([[1,1],[1,1]],board)
    def test03(self):
        board=[[0,1,0],[0,0,1],[1,1,1]]
        get_sol().gameOfLife(board)
        self.assertEqual([[0,0,0],[1,0,1],[0,1,1]],board)
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):

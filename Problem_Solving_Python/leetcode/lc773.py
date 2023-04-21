import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution2()
class Solution2:
    # bfs
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def within(x,y): return 0<=x<2 and 0<=y<3
        def get_moves(x,y): return [(x+dx,y+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)] if within(x+dx,y+dy)]
        def getZeroPos(brd): return [[i,j] for i in range(2) for j in range(3) if brd[i][j]==0][0]
        def serialize(brd): return tuple([tuple(row[:]) for row in brd])
        def deserialize(tup): return [list(row) for row in tup]
        def get_neighbors(boardTup:tuple[tuple]):
            li = []
            x,y=getZeroPos(boardTup)
            for i,j in get_moves(x,y):
                brdCopyList = deserialize(boardTup)
                brdCopyList[x][y],brdCopyList[i][j]=brdCopyList[i][j],brdCopyList[x][y] # swap
                li.append(serialize(brdCopyList))
            return li


        q = deque()
        vis=set()
        q.append(serialize(board))
        target = ((1,2,3),(4,5,0))
        res=0
        while q:
            for _ in range(len(q)):
                board = q.popleft()
                if board==target: return res
                if board in vis: continue
                vis.add(board)
                q.extend(get_neighbors(board))
            res+=1
        return -1
class Solution:
    # bfs
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def h(board:List[List[int]]): # list to tuple
            return tuple(tuple(x) for x in board)
        def invh(tup_board:tuple): # tuple to list
            return [list(x) for x in tup_board]
        def swap_pieces(board:List[List[int]],x1,y1,x2,y2):
            board[x1][y1],board[x2][y2]=board[x2][y2],board[x1][y1]
            return board
        def find_zero(board):
            for i in range(3):
                for j in range(3):
                    if board[i][j]==0:
                        return [i,j]


        vis=set()
        res = 0
        q = deque([h(board)])
        while q:
            for _ in range(len(q)):
                board = q.popleft()
                if board in vis: continue
                vis.add(board)
                if board==((1,2,3),(4,5,0)): return res
                x,y=find_zero(board)
                for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                    new_x,new_y=x+dx,y+dy
                    if not 0<=new_x<2 or not 0<=new_y<3: continue
                    new_board = swap_pieces(invh(board),x,y,new_x,new_y)
                    new_board=h(new_board)
                    q.append(new_board)
            res+=1
        return -1

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().slidingPuzzle([[1,2,3],[4,0,5]]))
    def test2(self):
        self.assertEqual(-1, get_sol().slidingPuzzle([[1,2,3],[5,4,0]]))
    def test3(self):
        self.assertEqual(5, get_sol().slidingPuzzle([[4,1,2],[5,0,3]]))
    def test4(self):
        self.assertEqual(14, get_sol().slidingPuzzle([[3,2,4],[1,5,0]]))
    def test5(self):
        self.assertEqual(0, get_sol().slidingPuzzle([[1,2,3],[4,5,0]]))
    # def test6(self):
    # def test7(self):
    # def test8(self):

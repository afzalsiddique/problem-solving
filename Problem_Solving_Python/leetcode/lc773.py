import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
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
        board = [[1,2,3],[4,0,5]]
        Output= 1
        self.assertEqual(Output, get_sol().slidingPuzzle(board))
    def test2(self):
        board = [[1,2,3],[5,4,0]]
        Output= -1
        self.assertEqual(Output, get_sol().slidingPuzzle(board))
    def test3(self):
        board = [[4,1,2],[5,0,3]]
        Output= 5
        self.assertEqual(Output, get_sol().slidingPuzzle(board))
    def test4(self):
        board = [[3,2,4],[1,5,0]]
        Output= 14
        self.assertEqual(Output, get_sol().slidingPuzzle(board))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

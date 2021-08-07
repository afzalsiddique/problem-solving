import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def checkMove(self, board: List[List[str]], r: int, c: int, color: str) -> bool:
        def valid(x,y):
            if 0<=x<8 and 0<=y<8: return True
            return False

        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        if board[r][c]!='.': return False
        # for x in board: print(x)
        opp_col='B' if color=='W' else 'W'
        def f(dx,dy):
            x,y=r,c
            x+=dx
            y+=dy
            cnt=0
            while valid(x,y) and board[x][y]==opp_col:
                cnt+=1
                x+=dx
                y+=dy
            if not valid(x,y): return False
            if not cnt: return False
            if board[x][y]==color: return True
            return False

        for dx,dy in dirs:
            if f(dx,dy): return True
        return False

class Tester(unittest.TestCase):
    def test_1(self):
        points = [[8,7],[9,9],[7,4],[9,7]]
        Output= 1
        self.assertEqual(Output,get_sol().maxWidthOfVerticalArea(points))
    def test_2(self):
        points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        Output= 3
        self.assertEqual(Output,get_sol().maxWidthOfVerticalArea(points))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

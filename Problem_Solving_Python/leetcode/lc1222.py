import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def inside_board(): return 0<=i<n and 0<=j<n
        def cell_is_not_queen(): return inside_board() and board[i][j]!=QUEEN
        def add():
            if inside_board() and board[i][j]==QUEEN: res.append([i,j])
        n=8
        QUEEN = 'q'
        board = [['.']*n for _ in range(n)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        for i,j in queens: board[i][j]=QUEEN

        res=[]
        for di,dj in dirs:
            i,j=king[0],king[1]
            while cell_is_not_queen():
                i+=di;j+=dj
            add()

        return res
class Solution2:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def inside_board(): return 0<=i<n and 0<=j<n
        def cell_is_not_queen(): return inside_board() and board[i][j]!=QUEEN
        def add():
            if inside_board() and board[i][j]==QUEEN: res.append([i,j])
        n=8
        QUEEN = 'q'
        # KING = 'k'
        board = [['.']*n for _ in range(n)]
        for i,j in queens: board[i][j]='q'
        # board[king[0]][king[1]]=KING
        # for x in board: print(''.join(x))

        res=[]
        # going down
        i,j=king[0],king[1]
        while cell_is_not_queen(): i+=1
        add()

        # going up
        i,j=king[0],king[1]
        while cell_is_not_queen(): i-=1
        add()

        # going right
        i,j=king[0],king[1]
        while cell_is_not_queen(): j+=1
        add()

        # going left
        i,j=king[0],king[1]
        while cell_is_not_queen(): j-=1
        add()

        # going down-right
        i,j=king[0],king[1]
        while cell_is_not_queen(): i+=1; j+=1
        add()

        # going up-right
        i,j=king[0],king[1]
        while cell_is_not_queen(): i-=1; j+=1
        add()

        # going down-left
        i,j=king[0],king[1]
        while cell_is_not_queen(): i+=1; j-=1
        add()

        # going up-left
        i,j=king[0],king[1]
        while cell_is_not_queen(): i-=1; j-=1
        add()

        return res

class tester(unittest.TestCase):
    def test_1(self):
        queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
        king = [0,0]
        Output= sorted([[0,1],[1,0],[3,3]])
        self.assertEqual(Output, sorted(get_sol().queensAttacktheKing(queens,king)))
    def test_2(self):
        queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
        king = [3,3]
        Output= sorted([[2,2],[3,4],[4,4]])
        self.assertEqual(Output, sorted(get_sol().queensAttacktheKing(queens,king)))
    def test_3(self):
        queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
        king = [3,4]
        Output= sorted([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]])
        self.assertEqual(Output, sorted(get_sol().queensAttacktheKing(queens,king)))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

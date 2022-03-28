from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution2()
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_square(i,j):
            return (i//3,j//3)
        row,col,square = defaultdict(set),defaultdict(set),defaultdict(set)
        for i in range(9):
            for j in range(9):
                temp=board[i][j]
                if temp=='.': continue
                sq = get_square(i,j)
                if temp in row[i] or temp in col[j] or temp in square[sq]:
                    return False
                row[i].add(temp)
                col[j].add(temp)
                square[sq].add(temp)
        return True
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows():
            for row in board:
                count=Counter(row)
                if any(count[c]>1 for c in map(str,range(1,9+1))):
                    return False
            return True
        def checkCols():
            for j in range(9):
                count=Counter(board[i][j] for i in range(9))
                if any(count[c]>1 for c in map(str,range(1,9+1))):
                    return False
            return True
        def checkSubGrid(x,y):
            count=Counter()
            for i in range(x*3,x*3+3):
                for j in range(y*3,y*3+3):
                    count[board[i][j]]+=1
            if any(count[c]>1 for c in map(str,range(1,9+1))):
                return False
            return True
        def checkAllSubGrids():
            for x in range(3):
                for y in range(3):
                    if not checkSubGrid(x,y):
                        return False
            return True

        return checkCols() and checkRows() and checkAllSubGrids()
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,get_sol().isValidSudoku([["5","3",".",".","7",".",".",".","."]
                                                          ,["6",".",".","1","9","5",".",".","."]
                                                          ,[".","9","8",".",".",".",".","6","."]
                                                          ,["8",".",".",".","6",".",".",".","3"]
                                                          ,["4",".",".","8",".","3",".",".","1"]
                                                          ,["7",".",".",".","2",".",".",".","6"]
                                                          ,[".","6",".",".",".",".","2","8","."]
                                                          ,[".",".",".","4","1","9",".",".","5"]
                                                          ,[".",".",".",".","8",".",".","7","9"]]))
    def test02(self):
        self.assertEqual(False,get_sol().isValidSudoku([["8","3",".",".","7",".",".",".","."]
                                                           ,["6",".",".","1","9","5",".",".","."]
                                                           ,[".","9","8",".",".",".",".","6","."]
                                                           ,["8",".",".",".","6",".",".",".","3"]
                                                           ,["4",".",".","8",".","3",".",".","1"]
                                                           ,["7",".",".",".","2",".",".",".","6"]
                                                           ,[".","6",".",".",".",".","2","8","."]
                                                           ,[".",".",".","4","1","9",".",".","5"]
                                                           ,[".",".",".",".","8",".",".","7","9"]]))

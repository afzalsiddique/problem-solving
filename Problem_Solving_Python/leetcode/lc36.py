import builtins
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List




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
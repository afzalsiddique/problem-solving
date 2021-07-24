import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m,n=len(A),len(A[0])
        # for every row, if the 0th col is 0, then flip everything in that row
        for i in range(m):
            if A[i][0]==0:
                for j in range(n):
                    A[i][j]^=1 # flip everything in ith row

        # for every col (except 0th col), if there are more zeros than ones then flip everything in that col
        for j in range(1,n):
            zero_cnt=0
            for i in range(m):
                if A[i][j]==0:
                    zero_cnt+=1
            if zero_cnt>m//2:
                for i in range(m):
                    A[i][j]^=1

        res=0
        for row in A:
            string = ''.join(list(map(str,row)))
            num = int(string,2)
            res+=num
        return res




class tester(unittest.TestCase):
    def test_1(self):
        grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        Output= 39
        self.assertEqual(Output, get_sol().matrixScore(grid))
    def test_2(self):
        grid = [[0]]
        Output= 1
        self.assertEqual(Output, get_sol().matrixScore(grid))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
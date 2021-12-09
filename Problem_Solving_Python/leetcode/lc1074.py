import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]

        res=0
        for i in range(n):
            for j in range(i,n):
                cur=0
                di=defaultdict(int)
                di[0]=1
                for k in range(m):
                    cur+=matrix[k][j] - (matrix[k][i-1] if i!=0 else 0)
                    res+=di[cur-target]
                    di[cur]+=1
        return res

class tester(unittest.TestCase):
    def test1(self):
        Output= 4
        self.assertEqual(Output,get_sol().numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))
    def test2(self):
        Output= 5
        self.assertEqual(Output,get_sol().numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))
    def test3(self):
        Output= 0
        self.assertEqual(Output,get_sol().numSubmatrixSumTarget(matrix = [[904]], target = 0))

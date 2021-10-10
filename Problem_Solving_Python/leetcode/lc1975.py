import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_neg = float('inf')
        min_pos = float('inf')
        cnt=0
        total_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<=0:
                    cnt+=1
                    min_neg = min(min_neg,abs(matrix[i][j]))
                if matrix[i][j]>=0:
                    min_pos = min(min_pos,matrix[i][j])
                total_sum+=abs(matrix[i][j])

        if cnt&1==0:
            return total_sum
        return total_sum-2*min(min_neg,min_pos)


class MyTestCase(unittest.TestCase):
    def test1(self):
        matrix = [[1,-1],[-1,1]]
        Output= 4
        self.assertEqual(Output, get_sol().maxMatrixSum(matrix))
    def test2(self):
        matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
        Output= 16
        self.assertEqual(Output, get_sol().maxMatrixSum(matrix))
    def test3(self):
        matrix = [[-1,0,-1],[-2,1,3],[3,2,2]]
        Output= 15
        self.assertEqual(Output, get_sol().maxMatrixSum(matrix))
    def test4(self):
        matrix = [[2,9,3],[5,4,-4],[1,7,1]]
        Output= 34
        self.assertEqual(Output, get_sol().maxMatrixSum(matrix))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

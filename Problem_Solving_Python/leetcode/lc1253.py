import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n=len(colsum)
        if sum(colsum)!=upper+lower: return []
        matrix=[[0]*n for _ in range(2)]
        for i in range(n):
            if colsum[i]==2:
                if not lower or not upper: return []
                matrix[0][i]=1
                matrix[1][i]=1
                upper-=1
                lower-=1
        for i in range(n):
            if colsum[i]==1:
                if not lower and not upper: return []
                if upper:
                    matrix[0][i]=1
                    upper-=1
                elif lower:
                    matrix[1][i]=1
                    lower-=1
        # for x in matrix: print(x)
        # print(upper)
        # print(lower)
        return matrix


class Tester(unittest.TestCase):
    def test_1(self):
        upper,lower,colsum = 2, 1,[1,1,1]
        Output= [[1,1,0],[0,0,1]]
        self.assertEqual(Output,get_sol().reconstructMatrix(upper,lower,colsum))
    def test_2(self):
        upper,lower,colsum = 2, 3,[2,2,1,1]
        Output= []
        self.assertEqual(Output,get_sol().reconstructMatrix(upper,lower,colsum))
    def test_3(self):
        upper,lower,colsum = 5, 5,[2,1,2,0,1,0,1,2,0,1]
        Output= [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
        self.assertEqual(Output,get_sol().reconstructMatrix(upper,lower,colsum))
    def test_4(self):
        upper,lower,colsum = 9, 2, [0,1,2,0,0,0,0,0,2,1,2,1,2]
        Output= []
        self.assertEqual(Output,get_sol().reconstructMatrix(upper,lower,colsum))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

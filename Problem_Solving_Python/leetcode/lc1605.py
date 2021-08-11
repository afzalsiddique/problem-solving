import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC++Python-Easy-and-Concise-with-Prove/719776
    # Trying to explain my intuition behind this solution:
    # For every cell, the value in it is constrained by the values of the rowSum and colSum. Moreover, the value is
    # constrained by the minimum of these two. For eg. if the rowSum=3 and colSum=4 for a particular cell,
    # then you can only take the values [0, 1, 2, 3] for that cell.
    # What if we greedily pick the largest value out of the possible values each time ?
    # Picking the largest value possible corresponds to picking the min(rowSum, colSum). Since total(rowSum) = total(
    # colSum), initially we had the equation that 3 + r2 + r3 + .. + rN = 4 + c2 + c3 + .. + cM. Since we use 3 as
    # the value for the current cell, our new equation becomes 0 + r2 + r3 + .. + rN = 1 + c2 + c3 + .. + cM,
    # which follows from the equation earlier. So as @lee215 mentioned, we haven't broken anything, the total(rowSum)
    # = total(colSum) condition still holds.
    # In this manner, for every cell we can continue to choose the minimum value, which would keep on decrementing a
    # value in the total(rowSum) = total(colSum) equation above. Eventually, our equation will decompose into just a
    # single value rn = cm. In which case we would just put the value at cell[n][m] = rn = cm.
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n=len(rowSum),len(colSum)
        mat=[[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                minn=min(rowSum[i],colSum[j])
                mat[i][j]=minn
                rowSum[i]-=minn
                colSum[j]-=minn
        return mat
class MyTestCase(unittest.TestCase):
    def test_1(self):
        rowSum = [3,8]
        colSum = [4,7]
        Output= [[3,0], [1,7]]
        self.assertEqual(Output, get_sol().restoreMatrix(rowSum,colSum))
    def test_2(self):
        rowSum = [5,7,10]
        colSum = [8,6,8]
        Output= [[0,5,0], [6,1,0], [2,0,8]]
        self.assertEqual(Output, get_sol().restoreMatrix(rowSum,colSum))
    def test_3(self):
        rowSum = [14,9]
        colSum = [6,9,8]
        Output= [[0,9,5], [6,0,3]]
        self.assertEqual(Output, get_sol().restoreMatrix(rowSum,colSum))
    def test_4(self):
        rowSum = [1,0]
        colSum = [1]
        Output= [[1], [0]]
        self.assertEqual(Output, get_sol().restoreMatrix(rowSum,colSum))
    def test_5(self):
        rowSum = [0]
        colSum = [0]
        Output= [[0]]
        self.assertEqual(Output, get_sol().restoreMatrix(rowSum,colSum))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
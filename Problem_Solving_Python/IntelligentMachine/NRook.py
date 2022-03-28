from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
def solution(A):
    m,n=len(A),len(A[0])
    rowMax=[float('-inf')]*m
    rowMaxIdx=[(-1,-1)]*m
    rowSecondMax=[float('-inf')]*m
    rowSecondMaxIdx=[(-1,-1)]*m
    for i in range(m):
        for j in range(n):
            if A[i][j]>=rowMax[i]:
                rowSecondMax[i]=rowMax[i]
                rowSecondMaxIdx[i]=rowMaxIdx[i]
                rowMax[i]=A[i][j]
                rowMaxIdx[i]=(i,j)


    colMax=[float('-inf')]*n
    colMaxIdx=[(-1,-1)]*n
    colSecondMax=[float('-inf')]*n
    colSecondMaxIdx=[(-1,-1)]*n

    for j in range(n):
        for i in range(m):
            if A[i][j]>=colMax[j]:
                colSecondMax[j]=colMax[j]
                colSecondMaxIdx[j]=colMaxIdx[j]
                colMax[j]=A[i][j]
                colMaxIdx[j]=(i,j)

    print(colMax)
    print(colMaxIdx)

    res=0
    for i in range(m):
        maxRow,maxCol=rowMaxIdx[i]
        a=rowMax[i]
        for j in range(n):
            firstMaxRow,firstMaxCol=colMaxIdx[j]
            b=colMax[j]
            if firstMaxRow!=maxRow and firstMaxCol!=maxCol:
                res=max(res,a+b)
            secondMaxRow,secondMaxCol=colSecondMaxIdx[j]
            b=colSecondMax[j]
            if secondMaxRow!=maxRow and secondMaxCol!=maxCol:
                res=max(res,a+b)
    return res


class Tester(unittest.TestCase):
    def test01(self):
        # 4 + 2
        self.assertEqual(6,solution([
            [1,4],
            [2,3]
        ]))
    def test02(self):
        # 15+8
        self.assertEqual(23,solution([
            [15,1,5],
            [16,3,8],
            [2,6,4]
        ]))
    def test03(self):
        # 12+12
        self.assertEqual(24,solution([
            [12,12],
            [12,12],
            [0,7]
        ]))
    def test04(self):
        # 14+8
        self.assertEqual(22,solution([
            [1,2,14],
            [8,3,15]
        ]))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):

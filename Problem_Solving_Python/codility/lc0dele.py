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

    for i in range(m):
        for j in range(n):
            if A[i][j]>=colMax[j]:
                colSecondMax[j]=colMax[j]
                colSecondMaxIdx[j]=colMaxIdx[j]
                colMax[j]=A[i][j]
                colMaxIdx[j]=(i,j)

    res=0
    for i in range(m):
        maxRow,maxCol=rowMaxIdx[i]
        a=rowMax[i]
        for j in range(n):
            firstMaxRow,firstMaxCol=colMaxIdx[j]
            b=colMax[j]
            if firstMaxRow!=maxRow and firstMaxCol!=firstMaxCol:
                res=max(res,a+b)
            secondMaxRow,secondMaxCol=colSecondMaxIdx[j]
            b=colSecondMax[j]
            if secondMaxRow!=maxRow and secondMaxCol!=maxCol:
                res=max(res,a+b)
    return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,solution([
            [1,5,2],
            [7,1,5],
            [8,1,9]
        ]))
    def test02(self):
        self.assertEqual(7,solution([5,3,8,3,2],2,5))
    def test03(self):
        self.assertEqual(12,solution([4,2,7],4,100))
    def test04(self):
        self.assertEqual(8,solution([2,2,1,2,2],2,3))
    def test05(self):
        self.assertEqual(4,solution([4,1,5,3],5,2))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):

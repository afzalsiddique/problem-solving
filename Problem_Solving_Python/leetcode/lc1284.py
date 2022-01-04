import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def singleFlip(mask,i,j):
            idx=i*n+j # flatten to 1d index
            return mask^(1<<idx)
        def flip(mask, i, j):
            mask=singleFlip(mask,i,j)
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                if not 0<=i+di<m or not 0<=j+dj<n: continue
                mask=singleFlip(mask,i+di,j+dj)
            return mask

        m,n=len(mat),len(mat[0])
        goal = 0
        initMask=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    initMask=singleFlip(initMask,i,j)

        q=deque([initMask])
        vis=set()
        vis.add(initMask)
        res=0
        while q:
            for _ in range(len(q)):
                mask=q.popleft()
                if mask==goal:
                    return res
                for i in range(m):
                    for j in range(n):
                        newMask=flip(mask,i,j)
                        if newMask not in vis:
                            q.append(newMask)
                            vis.add(newMask)
            res+=1
        return -1
class Solution2:
    def minFlips(self, mat: List[List[int]]) -> int:
        def makeTuple(mat: List[List[int]]):
            li=[tuple(row) for row in mat]
            return tuple(li)
        def getMatrix(tup):
            return [list(row) for row in tup]
        def flip(tup,i,j):
            mat=getMatrix(tup)
            mat[i][j]^=1
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                if not 0<=i+di<m or not 0<=j+dj<n: continue
                mat[i+di][j+dj]^=1
            return makeTuple(mat)

        m,n=len(mat),len(mat[0])
        goal = makeTuple([[0]*n for _ in range(m)])
        initial=makeTuple(mat)
        q=deque([initial])
        vis=set()
        vis.add(initial)
        res=0
        while q:
            for _ in range(len(q)):
                tup=q.popleft()
                if tup==goal:
                    return res
                for i in range(m):
                    for j in range(n):
                        tmp=flip(tup,i,j)
                        if tmp not in vis:
                            q.append(tmp)
                            vis.add(tmp)
            res+=1
        return -1



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minFlips([[0,0],[0,1]]))
    def test2(self):
        self.assertEqual(0, get_sol().minFlips([[0]]))
    def test3(self):
        self.assertEqual(-1, get_sol().minFlips([[1,0,0],[1,0,0]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

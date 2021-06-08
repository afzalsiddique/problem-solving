import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m,n=len(mat),len(mat[0])
        def rotate(mat):
            new_mat=[[None]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    new_mat[i][j]=mat[j][i]
            for i in range(m):
                new_mat[i].reverse()
            return new_mat

        new_mat = mat
        for _ in range(4):
            new_mat = rotate(new_mat)
            if new_mat==target:
                return True
        return False


class tester(unittest.TestCase):
    def test1(self):
        mat = [[0,1],[1,0]]
        target = [[1,0],[0,1]]
        Output= True
        self.assertEqual(Output,get_sol().findRotation(mat,target))

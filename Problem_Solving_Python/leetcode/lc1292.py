import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n=len(mat),len(mat[0])
        sums= [[0]*(n+1) for _ in range(m+1)]
        maxx = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + mat[i-1][j-1]
                if i-maxx-1>=0 and j-maxx-1>=0 and sums[i][j]- sums[i-maxx-1][j] - sums[i][j-maxx-1] + sums[i-maxx-1][j-maxx-1] <= threshold:
                    maxx += 1
        # for x in sums: print(x)
        return maxx
class Solution2:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n=len(mat),len(mat[0])
        sums= [[0]*(n+1) for _ in range(m+1)]
        maxx = 0

        for i in range(m):
            for j in range(n):
                sums[i+1][j+1] = sums[i+1][j] + sums[i][j+1] - sums[i][j] + mat[i][j]
                if i-maxx>=0 and j-maxx>=0 and sums[i+1][j+1] - sums[i-maxx][j+1] - sums[i+1][j-maxx] + sums[i-maxx][j-maxx] <= threshold:
                    maxx += 1
        # for x in sums: print(x)
        return maxx

class Tester(unittest.TestCase):
    def test1(self):
        mat,threshold = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4
        Output= 2
        self.assertEqual(Output,get_sol().maxSideLength(mat,threshold))
    def test2(self):
        mat,threshold = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1
        Output= 0
        self.assertEqual(Output,get_sol().maxSideLength(mat,threshold))
    def test3(self):
        mat,threshold = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6
        Output= 3
        self.assertEqual(Output,get_sol().maxSideLength(mat,threshold))
    def test4(self):
        mat,threshold = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184
        Output= 2
        self.assertEqual(Output,get_sol().maxSideLength(mat,threshold))
    # def test5(self):
    # def test6(self):
    # def test7(self):
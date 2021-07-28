import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
# class Solution:
    # try O(mn) solution later
class Solution:
    # https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721266/C%2B%2B-Understand-the-brute-force-solution-first!
    def numSubmat(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        def count(i, j): # count no of sub matrices whose top-left is at (i,j)
            bound=n
            cnt=0
            for x in range(i, m):
                y=j
                while y<bound:
                    if mat[x][y]==0:
                        bound = y
                    else:
                        cnt+=1
                    y+=1
            return cnt

        res=0
        for i in range(m):
            for j in range(n):
                res+=count(i,j)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        mat = [[1,0,1], [1,1,0], [1,1,0]]
        Output= 13
        self.assertEqual(Output,get_sol().numSubmat(mat))
    def test_2(self):
        mat = [[0,1,1,0], [0,1,1,1], [1,1,1,0]]
        Output= 24
        self.assertEqual(Output,get_sol().numSubmat(mat))
    def test_3(self):
        mat = [[1,1,1,1,1,1]]
        Output= 21
        self.assertEqual(Output,get_sol().numSubmat(mat))
    def test_4(self):
        mat = [[1,0,1],[0,1,0],[1,0,1]]
        Output= 5
        self.assertEqual(Output,get_sol().numSubmat(mat))
    # def test_5(self):
    # def test_6(self):
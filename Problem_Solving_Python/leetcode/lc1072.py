import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/discuss/303897/Java-easy-solution-%2B-explanation
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        maxx=0
        for i in range(m):
            cnt=0
            row=matrix[i]
            invert_row = [1^x for x in row]
            for j in range(m):
                if matrix[j]==row or matrix[j]==invert_row:
                    cnt+=1
                    maxx=max(maxx,cnt)
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[0,1],[1,1]]
        Output= 1
        self.assertEqual(Output, get_sol().maxEqualRowsAfterFlips(matrix))
    def test_2(self):
        matrix = [[0,1],[1,0]]
        Output= 2
        self.assertEqual(Output, get_sol().maxEqualRowsAfterFlips(matrix))
    def test_3(self):
        matrix = [[0,0,0],[0,0,1],[1,1,0]]
        Output= 2
        self.assertEqual(Output, get_sol().maxEqualRowsAfterFlips(matrix))
    def test_4(self):
        matrix = [[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]]
        Output= 2
        self.assertEqual(Output, get_sol().maxEqualRowsAfterFlips(matrix))
    # def test_5(self):
    # def test_6(self):
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020710/C%2B%2B-Clean-and-Clear-With-Intuitive-Pictures-O(m-*-n-*-logn)
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        heights=[0]*n
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    heights[j]=0
                else:
                    heights[j]+=1
            tmp_heights = [x for x in heights]
            tmp_heights.sort()
            for j in range(n):
                ans = max(ans,tmp_heights[j]*(n-j))
        return ans
class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[0,0,1],[1,1,1],[1,0,1]]
        Output= 4
        self.assertEqual(Output, get_sol().largestSubmatrix(matrix))
    def test_2(self):
        matrix = [[1,0,1,0,1]]
        Output= 3
        self.assertEqual(Output, get_sol().largestSubmatrix(matrix))
    def test_3(self):
        matrix = [[1,1,0],[1,0,1]]
        Output= 2
        self.assertEqual(Output, get_sol().largestSubmatrix(matrix))
    def test_4(self):
        matrix = [[0,0],[0,0]]
        Output= 0
        self.assertEqual(Output, get_sol().largestSubmatrix(matrix))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
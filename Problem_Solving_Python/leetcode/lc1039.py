import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286753/C%2B%2B-with-picture
    def minScoreTriangulation(self, A):
        def helper(begin, end):
            if end-begin+1 <= 2: return 0
            key = (begin,end)
            if key in memo: return memo[key]

            result = float("inf")
            for mid in range(begin+1, end):
                result = min(result, helper(begin, mid) + A[begin] * A[mid] * A[end] + helper(mid, end))
            memo[key] = result
            return memo[key]

        memo = {}
        return helper(0,len(A)-1)



class Tester(unittest.TestCase):
    def test_1(self):
        values = [1,2,3]
        Output= 6
        self.assertEqual(Output,get_sol().minScoreTriangulation(values))
    def test_2(self):
        values = [3,7,4,5]
        Output= 144
        self.assertEqual(Output,get_sol().minScoreTriangulation(values))
    def test_3(self):
        values = [5,3,2,4,6]
        Output= 138
        self.assertEqual(Output,get_sol().minScoreTriangulation(values))
    def test_4(self):
        values = [1,3,1,4,1,5]
        Output= 13
        self.assertEqual(Output,get_sol().minScoreTriangulation(values))
    def test_5(self):
        values = [1,3,3,5,2]
        Output= 34
        self.assertEqual(Output,get_sol().minScoreTriangulation(values))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

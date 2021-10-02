from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        if length!=m*n: return []
        mat = [[0]*n for _ in range(m)]
        for i in range(length):
            mat[i//n][i%n]=original[i]
        return mat

class MyTestCase(unittest.TestCase):
    def test_1(self):
        original = [1,2,3,4]
        m = 2
        n = 2
        Output= [[1,2],[3,4]]
        self.assertEqual(Output, get_sol().construct2DArray(original,m,n))
    def test_2(self):
        original = [1,2,3]
        m = 1
        n = 3
        Output= [[1,2,3]]
        self.assertEqual(Output, get_sol().construct2DArray(original,m,n))
    def test_3(self):
        original = [1,2]
        m = 1
        n = 1
        Output= []
        self.assertEqual(Output, get_sol().construct2DArray(original,m,n))
    def test_4(self):
        original = [3]
        m = 1
        n = 2
        Output= []
        self.assertEqual(Output, get_sol().construct2DArray(original,m,n))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

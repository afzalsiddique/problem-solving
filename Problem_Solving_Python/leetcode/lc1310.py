import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # similar to prefix_sum
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor=list(itertools.accumulate(arr,lambda x,y:x^y))
        res=[]
        for l,r in queries:
            res.append(pre_xor[r]^pre_xor[l]^arr[l])
        return res

class tester(unittest.TestCase):
    def test_1(self):
        arr = [1,3,4,8]
        queries = [[0,1],[1,2],[0,3],[3,3]]
        Output= [2,7,14,8]
        self.assertEqual(Output, get_sol().xorQueries(arr,queries))
    def test_2(self):
        arr = [4,8,2,10]
        queries = [[2,3],[1,3],[0,0],[0,3]]
        Output= [8,0,4,4]
        self.assertEqual(Output, get_sol().xorQueries(arr,queries))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
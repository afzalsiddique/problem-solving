from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def maximumGood(self, mat: List[List[int]]) -> int:
        G,B,N=1,0,2
        def check(li:List[int]):
            for i in range(n):
                if li[i] == G:
                    for j in range(n):
                        if mat[i][j]!=N and mat[i][j]!=li[j]:
                            return -1
            return sum(li[i]==G for i in range(n))
        def backtrack(li:List[int]):
            nonlocal maxx
            tmp=check(li)
            if tmp==-1:
                return
            maxx=max(maxx,tmp)


        n=len(mat)
        maxx=float('-inf')

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().maximumGood([[2,1,2],[1,2,2],[2,0,2]]))
    def test02(self):
        self.assertEqual(1,get_sol().maximumGood([[2,0],[0,2]]))
    # def test03(self):
    # def test04(self):
    # def test05(self):

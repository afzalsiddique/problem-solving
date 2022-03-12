from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m,n=len(A),len(B)
        A=[-1] + A # insert a dummy value at the beginning
        B=[-1] + B
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i]==B[j]:
                    dp[i][j]=1+dp[i-1][j-1]
        return max(map(max,dp))


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().findLength([1,2,3,2,1],[3,2,1,4,7]))
    def test02(self):
        self.assertEqual(5,get_sol().findLength([0,0,0,0,0],[0,0,0,0,0]))
    def test03(self):
        self.assertEqual(2,get_sol().findLength([0,1,1,1,1],[1,0,1,0,1]))
    def test04(self):
        self.assertEqual(3,get_sol().findLength([1,0,0,0,1],[1,0,0,1,1]))
    def test05(self):
        self.assertEqual(4,get_sol().findLength([0,0,1,0,0], [0,0,1,0]))



from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(i,m):
            if i==n:
                return 0
            res=float('-inf')
            summ=0
            for j in range(1,2*m+1): # j denotes number of piles taken
                if i+j>n: break
                summ+=piles[i+j-1]
                take=summ
                # take-dp(..) -> myScore-Opponent's score.
                res=max(res,take-dp(i+j,max(m,j)))
            return res

        n=len(piles)
        moreAlice=dp(0,1)

        total = sum(piles)
        bobScore=(total-moreAlice)//2
        aliceScore=bobScore+moreAlice
        return aliceScore


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().stoneGameII([2,7,9]))
    def test02(self):
        self.assertEqual(104, get_sol().stoneGameII([1,2,3,4,5,100]))
    def test03(self):
        self.assertEqual(9, get_sol().stoneGameII([2,7,9,4]))
    def test04(self):
        self.assertEqual(10, get_sol().stoneGameII([2,7,9,4,4]))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

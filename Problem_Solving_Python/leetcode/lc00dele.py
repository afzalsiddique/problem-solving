from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[None]*(n+1)
        dp[0]=False
        for stone in range(1,n+1):
            i=1
            ans=False
            while stone-i*i>=0:
                remainingStones=stone-i*i
                if dp[remainingStones]==False:
                    ans=True
                    break
                i+=1
            dp[stone]=ans
        return dp[-1]


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().winnerSquareGame(1))
    def test02(self):
        self.assertEqual(False, get_sol().winnerSquareGame(2))
    def test03(self):
        self.assertEqual(True, get_sol().winnerSquareGame(3))
    def test04(self):
        self.assertEqual(True, get_sol().winnerSquareGame(4))
    def test05(self):
        self.assertEqual(False, get_sol().winnerSquareGame(5))
    def test06(self):
        self.assertEqual(True, get_sol().winnerSquareGame(6))
    def test07(self):
        self.assertEqual(False, get_sol().winnerSquareGame(7))
    def test08(self):
        self.assertEqual(True, get_sol().winnerSquareGame(8))
    def test09(self):
        self.assertEqual(True, get_sol().winnerSquareGame(9))
    def test10(self):
        self.assertEqual(False, get_sol().winnerSquareGame(10))
    def test11(self):
        self.assertEqual(True, get_sol().winnerSquareGame(92719))


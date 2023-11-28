from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        M=10**9+7
        ways=[[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1,m+1):
            ways[1][j][1]=1

        for a in range(1,n+1):
            for b in range(1,m+1):
                for c in range(1,k+1):
                    ways[a][b][c]+=b*ways[a-1][b][c]
                    for x in range(b):
                        ways[a][b][c]+=ways[a-1][x][c-1]
        return sum(ways[-1][j][k] for j in range(m+1))%M




class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(6, get_sol().numOfArrays(2, 3, 1))
    def test02(self):
        self.assertEqual(0, get_sol().numOfArrays(5, 2, 3))
    def test03(self):
        self.assertEqual(1, get_sol().numOfArrays(9, 1, 1))
    def test04(self):
        self.assertEqual(7, get_sol().numOfArrays(4, 2, 2))
    def test05(self):
        self.assertEqual(39, get_sol().numOfArrays(4, 3, 2))
    # def test06(self):
    # def test07(self):
    # def test08(self):

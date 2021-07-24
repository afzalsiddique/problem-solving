import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        piles.sort(reverse=True)
        # print(piles)
        li = [piles[i] for i in range(1,2*n+1,2)]
        # print(li)
        return sum(li)

class tester(unittest.TestCase):
    def test_1(self):
        piles = [2,4,1,2,7,8]
        Output= 9
        self.assertEqual(Output, get_sol().maxCoins(piles))
    def test_2(self):
        piles = [2,4,5]
        Output= 4
        self.assertEqual(Output, get_sol().maxCoins(piles))
    def test_3(self):
        piles = [9,8,7,6,5,1,2,3,4]
        Output= 18
        self.assertEqual(Output, get_sol().maxCoins(piles))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
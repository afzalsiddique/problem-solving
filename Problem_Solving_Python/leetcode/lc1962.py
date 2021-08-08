import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq=[-x for x in piles]
        total=sum(piles)
        heapify(pq)
        while k and pq:
            tmp=heappop(pq)
            tmp*= (-1)
            total-=tmp//2
            tmp-=tmp//2
            if tmp!=1:
                heappush(pq,-tmp)
            k-=1
        return total


class Tester(unittest.TestCase):
    def test_1(self):
        piles = [5,4,9]
        k = 2
        Output= 12
        self.assertEqual(Output,get_sol().minStoneSum(piles,k))
    def test_2(self):
        piles = [4,3,6,7]
        k = 3
        Output= 12
        self.assertEqual(Output,get_sol().minStoneSum(piles,k))
    def test_3(self):
        piles = [1]
        k = 100000
        Output= 1
        self.assertEqual(Output,get_sol().minStoneSum(piles,k))
    def test_4(self):
        piles = [10000]
        k = 10000
        Output= 1
        self.assertEqual(Output,get_sol().minStoneSum(piles,k))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

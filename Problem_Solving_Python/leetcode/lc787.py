from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """ O(k*E)T O(V)S bellman-ford algo """
        cost = defaultdict(lambda: float('-inf'))
        cost[src] = 0
        for _ in range(k + 1):
            cost_ = cost.copy()
            for a, b, c in flights:
                if cost_[b] > cost[a] + c:
                    cost_[b] = cost[a] + c
            cost = cost_

        return cost[dst] if cost[dst] != float('-inf') else -1

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,1,1,0],get_sol().countSmaller([5,2,6,1]))
    def test02(self):
        self.assertEqual([0],get_sol().countSmaller([-1]))
    def test03(self):
        self.assertEqual([0,0],get_sol().countSmaller([-1,-1]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res=0
        for i in range(len(cost)):
            if i%3==0 or i%3==1:
                res+=cost[i]
        return res

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(5,get_sol().minimumCost([1,2,3]))
    def test02(self):
        self.assertEqual(23,get_sol().minimumCost([6,5,7,9,2,2]))
    def test03(self):
        self.assertEqual(10,get_sol().minimumCost([5,5]))
    def test04(self):
        self.assertEqual(1,get_sol().minimumCost([1]))
    # def test05(self):

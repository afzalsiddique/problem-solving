from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx,total,left=0,0,0
        for i in range(len(cost)):
            left = left + gas[i] - cost[i]
            total = total + gas[i] - cost[i]
            if left<0:
                left=0
                idx=i+1
        return idx if total>=0 else -1

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    def test02(self):
        self.assertEqual(-1, get_sol().canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
    def test03(self):
        self.assertEqual(0, get_sol().canCompleteCircuit(gas = [2,3,4], cost = [2,3,4]))

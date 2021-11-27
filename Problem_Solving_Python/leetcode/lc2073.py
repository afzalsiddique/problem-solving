import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i,x in enumerate(tickets):
            if i<k:
                res += min(tickets[i],tickets[k])
            elif i==k:
                res += tickets[i]
            else:
                if tickets[i]>=tickets[k]:
                    res += tickets[k]-1
                else:
                    res += tickets[i]
        return res



class MyTestCase(unittest.TestCase):
    def test1(self):
        tickets, k = [2,3,2] ,2
        Output= 6
        self.assertEqual(Output, get_sol().timeRequiredToBuy(tickets,k))
    def test2(self):
        tickets,k = [5,1,1,1],  0
        Output= 8
        self.assertEqual(Output, get_sol().timeRequiredToBuy(tickets,k))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):

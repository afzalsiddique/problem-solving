from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(x): return solution(x)
def solution(N):
    length=32
    res=0
    cnt=float('-inf')
    for i in range(length):
        if (N>>i) & 1==0:
            cnt+=1
        else:
            res=max(res,cnt)
            cnt=0
    return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol(9))
    def test02(self):
        self.assertEqual(4,get_sol(529))
    def test03(self):
        self.assertEqual(1,get_sol(20))
    def test04(self):
        self.assertEqual(0,get_sol(0))
    def test05(self):
        self.assertEqual(0,get_sol(1))
    def test06(self):
        self.assertEqual(0,get_sol(2))

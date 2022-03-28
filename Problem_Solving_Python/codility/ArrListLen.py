from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(a): return solution(a)
def solution(A):
    idx=0
    res=1
    while A[idx]!=-1:
        res+=1
        idx=A[idx]
    return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual( 4,get_sol([1, 4, -1, 3, 2]))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
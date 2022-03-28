from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(a,b,c): return solution(a,b,c)
def solution(A, B, C):
    # https://stackoverflow.com/questions/10401239/count-bitmasks-enumerate-0s
    N=30
    def supers(A):
        zeros = sum(1 for i in range(N) if (A>>i)&1==0)
        return 2**zeros

    res=0
    res+=supers(A)
    res+=supers(B)
    res+=supers(C)
    res-=supers(A|B)
    res-=supers(B|C)
    res-=supers(C|A)
    res+=supers(A|B|C)
    return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual( 8,get_sol(1073741727,1073741631,1073741679))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
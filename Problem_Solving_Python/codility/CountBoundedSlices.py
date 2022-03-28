from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(a,b): return solution(b, a)
def solution(k, A):
    # https://stackoverflow.com/questions/21251707/counting-bounded-slice-codility
    # performance 60%
    def triangular(n): return n*(n+1)//2
    n=len(A)
    result=0
    i=0
    while i<n:
        lower = A[i]
        upper = A[i]
        countBackw = 0
        countForw = 0
        for j in range(i-1,-1,-1):
            if A[j] < lower:
                if upper - A[j] > k:
                    break
                else:
                    lower = A[j]
            elif A[j] > upper:
                if A[j] - lower > k:
                    break
                else:
                    upper = A[j]
            countBackw+=1

        for j in range(i,n):
            if A[j] < lower:
                if upper - A[j] > k:
                    break
                else:
                    lower = A[j]
            elif A[j] > upper:
                if A[j] - lower > k:
                    break
                else:
                    upper = A[j]
            countForw+=1
        result -= triangular(countBackw)
        result += triangular(countForw + countBackw)
        i+= countForw
    return result

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(9,get_sol([3,5,7,6,3],2))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(a,b): return solution(b, a)
def solution(K, A):
    N = len(A)

    maxQ = [0] * (N + 1)
    posmaxQ = [0] * (N + 1)
    minQ = [0] * (N + 1)
    posminQ = [0] * (N + 1)

    firstMax, lastMax = 0, -1
    firstMin, lastMin = 0, -1
    j, result = 0, 0

    for i in range(N):
        while (j < N):
            # added new maximum element
            while lastMax >= firstMax and maxQ[lastMax] <= A[j]:
                lastMax -= 1
            lastMax += 1
            maxQ[lastMax] = A[j]
            posmaxQ[lastMax] = j
            # added new minimum element
            while lastMin >= firstMin and minQ[lastMin] >= A[j]:
                lastMin -= 1
            lastMin += 1
            minQ[lastMin] = A[j]
            posminQ[lastMin] = j

            if maxQ[firstMax] - minQ[firstMin] <= K:
                j += 1
            else:
                break
        result += (j - i)
        if posminQ[firstMin] == i:
            firstMin += 1
        if posmaxQ[firstMax] == i:
            firstMax += 1
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

# from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
import heapq
# n,k = list(map(int,input().split()))
li = list(map(int,input().split()))
print(li)
pq = []
for i in range(n):
    heapq.heappush(pq,li[i])
    if len(pq)>k:
        heapq.heappop(pq)
res=None
while pq:
    res=heapq.heappop(pq)
print(res)
# return res

def takeInput():
    n,k = list(map(int,input().split()))
    li = list(map(int,input().split()))


# class MyTestCase(unittest.TestCase):
#     def test01(self):
#         self.assertEqual(97,myFunc(15,1,))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):

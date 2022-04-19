# from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
n=int(input())
li = list(map(int,input().split()))
prev=float('-inf')
flag='Yes'
for i in range(n):
    if li[i]<prev:
        flag='No'
        break
    prev=li[i]
print(flag)


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

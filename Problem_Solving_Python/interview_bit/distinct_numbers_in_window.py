from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
def get_sol(): return Solution()
class Solution:
    def dNums(self, A, k):
        n=len(A)
        res=[]
        count=Counter()
        unique=0
        for i in range(k-1):
            if count[A[i]]==0: unique+=1
            count[A[i]]+=1

        for i in range(k-1,n):
            if count[A[i]]==0: unique+=1
            count[A[i]]+=1

            res.append(unique)

            count[A[i-k+1]]-=1
            if count[A[i-k+1]]==0: unique-=1
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([2, 3, 3, 2],get_sol().dNums([1, 2, 1, 3, 4, 3],3))
    def test02(self):
        self.assertEqual([1],get_sol().dNums([87],1))

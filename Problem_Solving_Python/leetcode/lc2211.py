from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def countCollisions(self, A: str) -> int:
        n=len(A)
        noCrash=0
        i=0
        while i<n and A[i]=='L':
            i+=1
        noCrash+=i
        i=n-1
        while i>=0 and A[i]=='R':
            i-=1
        noCrash+=(n-1)-i

        # for i in range(n):
        #     if A[i]!='S': continue
        #     safe=True
        #     if i-1>=0 and A[i-1]=='R':
        #         safe=False
        #     if i+1<n and A[i+1]=='L':
        #         safe=False
        #     if safe:
        #         noCrash+=1
        for i in range(n):
            if A[i]=='S':
                noCrash+=1
        return n-noCrash


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(5,get_sol().countCollisions("RLRSLL"))
    def test02(self):
        self.assertEqual(0,get_sol().countCollisions("LLRR"))
    def test03(self):
        self.assertEqual(0,get_sol().countCollisions("S"))
    def test04(self):
        self.assertEqual(0,get_sol().countCollisions("SS"))
    def test05(self):
        self.assertEqual(1,get_sol().countCollisions("SLS"))

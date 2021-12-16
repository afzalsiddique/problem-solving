import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @functools.lru_cache(None)
        def func(ring:str, j:int):
            if j==n: return 0
            ans=float('inf')
            for i in range(m):
                if ring[i]==key[j]:
                    tmp2=1+min(i,m-i)
                    tmp=tmp2+func(ring[i:]+ring[:i],j+1)
                    ans=min(ans,tmp)
            return ans

        m,n=len(ring),len(key)
        return func(ring,0)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().findRotateSteps(ring = "godding", key = "gd"))
    def test2(self):
        self.assertEqual(13,get_sol().findRotateSteps(ring = "godding", key = "godding"))
    def test3(self):
        self.assertEqual(137,get_sol().findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

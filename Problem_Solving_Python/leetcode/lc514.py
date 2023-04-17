from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dp(key_i, ring_i):
            res=float('inf')
            if key_i==len(key): return 0
            for new_ring_i in range(m):
                if key[key_i]==ring[new_ring_i]:
                    diff1=abs(new_ring_i-ring_i)
                    diff2=abs(new_ring_i-ring_i+m)
                    diff3=abs(ring_i-new_ring_i+m)
                    minDiff=min(diff1,diff2,diff3)
                    res=min(res,minDiff+dp(key_i+1,new_ring_i))
            return res

        return dp(0,0)+len(key)
class Solution2:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
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
    def test4(self):
        self.assertEqual(6,get_sol().findRotateSteps("nyngl", "ynl"))
    def test5(self):
        self.assertEqual(19,get_sol().findRotateSteps("nyngl", "yyynnnnnnlllggg"))
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

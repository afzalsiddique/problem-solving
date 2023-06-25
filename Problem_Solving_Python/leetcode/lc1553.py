from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dp(n):
            if n==0: return 0
            res=float('inf')

            if n%2==0: res=min(res,1+dp(n//2))
            if n%2==1: res=min(res,1+dp(n-1))

            if n%3==0: res=min(res,1+dp(n//3))
            if n%3==1: res=min(res,1+dp(n-1))
            if n%3==2: res=min(res,2+dp(n-2))
            # if n%3==2: res=min(res,1+dp(n-1)) # alternative
            return res

        return dp(n)
class Solution3:
    # dp
    def minDays(self, n: int) -> int:
        @cache
        def func(num:int):
            if num==0: return 0 # remaining 0
            return 1+min(num%2+func(num//2), num%3+func(num//3))

        return func(n)-1
class Solution2:
    # bad solution. bfs
    def minDays(self, n: int) -> int:
        q=deque()
        q.append(n)
        vis={n}
        res=0
        while q:
            for _ in range(len(q)):
                num = q.popleft()
                if num==0: return res
                if num-1 not in vis:
                    q.append(num-1)
                    vis.add(num-1)
                if num%2==0 and num%2 not in vis:
                    q.append(num//2)
                    vis.add(num//2)
                if num%3==0 and num%3 not in vis:
                    q.append(num-2*(num//3))
                    vis.add(num-2*(num//3))
            res+=1


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, get_sol().minDays(10))
    def test2(self):
        self.assertEqual(3, get_sol().minDays(6))
    def test3(self):
        self.assertEqual(8, get_sol().minDays(100))
    def test4(self):
        self.assertEqual(11, get_sol().minDays(553))
    def test5(self):
        self.assertEqual(22, get_sol().minDays(820592))
    def test6(self):
        self.assertEqual(1, get_sol().minDays(1))
    def test7(self):
        self.assertEqual(2, get_sol().minDays(2))
    def test8(self):
        self.assertEqual(2, get_sol().minDays(3))
    def test9(self):
        self.assertEqual(3, get_sol().minDays(4))
    def test10(self):
        self.assertEqual(4, get_sol().minDays(5))
    def test11(self):
        self.assertEqual(15, get_sol().minDays(19786))

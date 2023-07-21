from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def f(u,t,par):
            found=False
            if u==target:
                found=True
            if t==0:
                return [found, 1 if found else 0]
            val=0
            for v in g[u]:
                if v==par:
                    continue
                newFound,newVal=f(v,t-1,u)
                if newFound:
                    found=newFound
                    val=newVal
                    break
            if found:
                length=len(g[u])-1
                if length:
                    val=val*(1/length)
                else:
                    val=1
            return [found,val]

        g={1:[]}
        for a,b in edges:
            if a in g:
                g[a].append(b)
                g[b]=[]
            else:
                g[b].append(a)
                g[a]=[]
        found,val=f(1,t,0)
        return val


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(0.5, get_sol().frogPosition(4, [[1,2],[1,4],[2,3]], 2, 4))
    def test02(self):
        self.assertEqual(0.5, get_sol().frogPosition(4, [[1,2],[1,4],[2,3]], 3, 4))
    def test03(self):
        self.assertEqual(0.0, get_sol().frogPosition(6, [[2,1],[4,1],[5,1],[3,1],[6,3]], 7, 3))
    def test04(self):
        self.assertEqual(1.0, get_sol().frogPosition(1, [], 1, 1))
    def test05(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,2],[4,3],[5,3],[6,5],[7,3],[8,4],[9,5]], 9, 1))
    def test06(self):
        self.assertEqual(0.0, get_sol().frogPosition(5, [[2,1],[3,2],[5,3],[4,5]], 4, 1))
    def test07(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
    def test08(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]], 1, 8))
    def test09(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
    def test10(self):
        self.assertEqual(0.3333333333333333, get_sol().frogPosition( 7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1,  7))

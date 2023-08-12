from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class UnionFind:
    def __init__(self):
        self.par={}
        self.size={}
    def __repr__(self): return str(self.par)
    def add(self,a):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def union(self,a,b):
        self.add(a),self.add(b)
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        self.add(a)
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def sameGroup(self,a,b): return self.find(a)==self.find(b)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:




class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([False,False,True],get_sol().areConnected(6, 2, [[1,4],[2,5],[3,6]]))
    def test2(self):
        self.assertEqual([True,True,True,True,True],get_sol().areConnected(6, 0,  [[4,5],[3,4],[3,2],[2,6],[1,3]]))
    def test3(self):
        self.assertEqual([False,False,False,False,False],get_sol().areConnected(5, 1, [[4,5],[4,5],[3,2],[2,3],[3,4]]))
    def test4(self):
        self.assertEqual([True,True,True,True,True,True],get_sol().areConnected(1000, 0, [[231,147],[877,685],[428,588],[654,7],[714,546],[693,965]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

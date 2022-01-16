import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n+1)]
        self.size=[1 for _ in range(n+1)]
    def find(self,a):
        pa=self.par[a]
        if a!=pa:
            self.par[a]=self.find(pa)
        return self.par[a]
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.size[a]+=self.size[b]
            self.par[b]=self.par[a]
    def sameGroup(self,a,b): return self.find(a)==self.find(b)
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        def gcd(a,b):
            if a>b: return gcd(b,a)
            if a==0: return b
            return gcd(b%a,a)

        uf=UnionFind(n)
        for u in range(threshold+1,n+1):
            i=2
            while u*i<=n:
                v=u*i
                uf.union(u,v)
                i+=1

        res=[]
        for u,v in queries:
            res.append(uf.sameGroup(u,v))
        return res

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

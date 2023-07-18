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
    def unionAll(self,li):
        if len(li)==0: return
        if len(li)==1:
            self.add(li[0])
            return
        first=li[0]
        for second in li[1:]:
            self.union(first,second)
    def size_of_groups(self):
        for a in self.par:
            self.find(a)
        count=Counter(self.par.values())
        return list(count.values())
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n=len(row)
        uf=UnionFind()
        for i in range(0,n,2):
            i1=row[i]//2
            i2=row[i+1]//2
            uf.union(i1,i2)

        sizes=uf.size_of_groups()
        return sum(sizes)-len(sizes)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minSwapsCouples(row = [0,2,1,3]))
    def test2(self):
        self.assertEqual(0, get_sol().minSwapsCouples(row = [3,2,0,1]))
    def test3(self):
        self.assertEqual(4, get_sol().minSwapsCouples(row = [5,6,4,0,2,1,9,3,8,7,11,10]))
    # def test4(self):
    #     self.assertEqual(1, get_sol().minSwapsCouples(s1 = "ab", s2 = "ba"))
    # def test5(self):
    #     self.assertEqual(1, get_sol().kSimilarity("cba", "abc"))
    # def test6(self):
    #     self.assertEqual(3, get_sol().kSimilarity("bccaba", "abacbc"))
    # def test7(self):
    #     self.assertEqual(3, get_sol().kSimilarity("aabccb", "bbcaca"))

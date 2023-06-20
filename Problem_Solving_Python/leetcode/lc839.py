import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
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
    def size_of_groups(self):
        for a in self.par:
            self.find(a)
        count=Counter(self.par.values())
        return list(count.values())
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a,b):
            cnt=0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt+=1
                if cnt>2:
                    return False
            return True

        n=len(strs)
        uf = UnionFind()
        for s in strs:
            uf.add(s)
        for i,a in enumerate(strs):
            for j in range(i+1,n):
                b=strs[j]
                if similar(a,b):
                    uf.union(a,b)
        return len(uf.size_of_groups())

class Solution2:
    def numSimilarGroups(self, strs: List[str]) -> int:
        root = {i:i for i in range(len(strs))}
        def find(x):
            p=root.get(x,x)
            if p==x: return p
            root[x] = find(p)
            return root[x]
        def union(x,y):
            root[find(x)]=find(y)
        def similar(a,b):
            a,b=list(a),list(b)
            cnt=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    cnt+=1
                    if cnt>2: return False
            return True # because a and b are anagrams

        for i,a in enumerate(strs):
            for j in range(i+1,len(strs)):
                b=strs[j]
                if similar(a,b):
                    union(i,j)

        return len({find(root[x]) for x in root})

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,get_sol().numSimilarGroups(strs = ["tars","rats","arts","star"]))
    def test2(self):
        self.assertEqual(1,get_sol().numSimilarGroups(strs = ["omv","ovm"]))
    def test3(self):
        self.assertEqual(5,get_sol().numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]))
    def test4(self):
        self.assertEqual(8,get_sol().numSimilarGroups(["dzqsu","udzqs","qzsud","sudzq","zsduq","duszq","sduqz","suqzd","szqdu","qzuds","dzqsu","uqdzs","zsduq","quzds"]))
    # def test5(self):
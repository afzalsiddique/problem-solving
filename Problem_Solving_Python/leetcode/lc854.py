from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://miro.medium.com/max/3000/1*MvTnZScOoc6P1ZQR7lzOHg.png
    # https://medium.com/@jolyon129/854-k-similar-strings-7b68772217d0
    def kSimilarity(self, s1: str, s2: str) -> int:
        q=deque()
        n=len(s1)
        s1=list(s1)
        q.append((s1,0))
        res=0
        while q:
            for _ in range(len(q)):
                s1,i=q.popleft()
                while i<n and s1[i]==s2[i]: # skip same chars
                    i+=1
                if i==n: return res
                j=i
                while i<n: # find the index of s2[j] in s1. this index is denoted by i.
                    if s1[i]==s2[i]: # skip same chars
                        i+=1
                        continue
                    if s1[i]==s2[j]:
                        s1Copy=s1[:]
                        s1Copy[i],s1Copy[j]=s1Copy[j],s1Copy[i]
                        q.append((s1Copy,j))
                    i+=1
            res+=1

class Solution2:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def removeSameCharsFromBeginning(l1:List[str], l2:List[str]): # ('abdc','abcd') -> ('dc','cd')
            indices = [i for i in range(len(l1)) if l1[i] != l2[i]]
            l1 = [l1[i] for i in indices]
            l2 = [l2[i] for i in indices]
            return [l1, l2]
        @cache
        def swapFirstCharOfS1(s1:str, s2:str):
            s1, s2 = removeSameCharsFromBeginning(list(s1), list(s2))
            n=len(s1)
            if n==0: return 0
            firstCharOfS2 = s2[0]
            indices = [i for i in range(n) if s1[i] == firstCharOfS2] # find indices of chars in s1 which is equal to first char of s2
            res=float('inf')
            newListOfS1 = [performSwap(s1, i) for i in indices]
            for newS1 in newListOfS1:
                res=min(res, swapFirstCharOfS1(''.join(newS1), ''.join(s2)))
            return res+1
        def performSwap(li,i):
            li = [x for x in li]
            li[0],li[i]=li[i],li[0]
            return li

        return swapFirstCharOfS1(s1,s2)

class UnionFind:
    # wrong. it might work if the letters are unique
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
class Solution3:
    # wrong. it might work if the letters are unique
    def kSimilarity(self, s1: str, s2: str) -> int:
        di1,di2 = defaultdict(list),defaultdict(list)
        for i1,c1 in enumerate(s1):
            di1[c1].append(i1)
        for i2,c2 in enumerate(s2):
            di2[c2].append(i2)

        uf = UnionFind()
        for c in sorted(di1.keys()):
            for idx1,idx2 in zip(di1[c],di2[c]):
                uf.union(idx1,idx2)

        sizes = uf.size_of_groups()
        return sum(sizes) - len(sizes)
class mytestcase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().kSimilarity(s1 = "ab", s2 = "ba"))
    def test02(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abc", s2 = "bca"))
    def test03(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abac", s2 = "baca"))
    def test04(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "aabc", s2 = "abca"))
    def test05(self):
        self.assertEqual(1, get_sol().kSimilarity("cba", "abc"))
    def test06(self):
        self.assertEqual(3, get_sol().kSimilarity("bccaba", "abacbc"))
    def test07(self):
        self.assertEqual(3, get_sol().kSimilarity("aabccb", "bbcaca"))
    def test08(self):
        self.assertEqual(1, get_sol().kSimilarity("abcbca", "ababcc"))
    def test09(self):
        self.assertEqual(11, get_sol().kSimilarity("accbadbbacadcdedaebc", "caeacbbacddceacadbbd"))
    def test10(self):
        self.assertEqual(6, get_sol().kSimilarity("baaabaabbbabbbabaaab", "babbbbbaabaabaaaabba"))
    def test11(self):
        self.assertEqual(9, get_sol().kSimilarity("babcccabcbcbcbbaaabb", "bbcbabbaaacccacbbbcb"))

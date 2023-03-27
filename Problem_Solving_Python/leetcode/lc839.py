import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
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
        Output= 2
        self.assertEqual(Output,get_sol().numSimilarGroups(strs = ["tars","rats","arts","star"]))
    def test2(self):
        Output= 1
        self.assertEqual(Output,get_sol().numSimilarGroups(strs = ["omv","ovm"]))
    def test3(self):
        Output = 5
        self.assertEqual(Output,get_sol().numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]))
    # def test4(self):
    #     self.assertEqual(Output,get_sol().numSimilarGroups(n = 1, k = 2))
    # def test5(self):
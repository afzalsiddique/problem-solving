from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
# if opposite value exits then xor it opposite bit to get highest value -> 0^1=1
def get_sol(): return Solution()
class TrieNode: # same as leetcode 421 + add go variable
    def __init__(self):
        self.child={}
        self.go=0 # goes through this node
    def insert(self, num, cnt):
        node = self
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.child: node.child[bit]=TrieNode()
            node = node.child[bit]
            node.go+=cnt

    def query(self, num):
        node = self
        if not node: return -1
        res=0
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in node.child and node.child[1-bit].go>0:
                node = node.child[1 - bit]
                res |= (1 << i)
            else:
                node = node.child[bit]
        return res

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        def dfs(u):
            trieRoot.insert(u, 1)
            for val,i in queryByNode[u]:
                res[i]= trieRoot.query(val)
            for v in g[u]:
                dfs(v)
            trieRoot.insert(u, -1)

        n=len(parents)
        g=[[] for _ in range(n)]
        queryByNode=[[] for _ in range(n)]
        root=-1
        for child,p in enumerate(parents):
            if p==-1: root=child
            else: g[p].append(child)

        for i,[u,val] in enumerate(queries):
            queryByNode[u].append([val,i])

        trieRoot=TrieNode()
        res=[-1]*len(queries)
        dfs(root)
        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,3,7],get_sol().maxGeneticDifference([-1,0,1,1], [[0,2],[3,2],[2,5]]))
    def test02(self):
        self.assertEqual([6,14,7],get_sol().maxGeneticDifference([3,7,-1,2,0,7,0,2], [[4,6],[1,15],[0,5]]))
    # def test03(self):
    # def test04(self):
    # def test05(self):

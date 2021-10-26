import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # left = get_size from recursion
    # right = get_size from recursion
    # up = n-(left+right+1)
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def get_size(i):
            if dp[i]!=-1: return dp[i]
            if len(g[i])==0:
                return 1
            elif len(g[i])==1:
                left = get_size(g[i][0])
                right = 0
            else: # len(g[i])==2:
                left = get_size(g[i][0])
                right = get_size(g[i][1])
            dp[i]=left+right+1
            return left+right+1


        n = len(parents)
        dp = [-1]*n
        g = defaultdict(list)
        for child, par in enumerate(parents):
            if par==-1: continue
            g[par].append(child)

        di = Counter()
        for i in range(n):
            if len(g[i])==0:
                left = 0
                right = 0
                up = n-1
            elif len(g[i])==2:
                left = get_size(g[i][0])
                right = get_size(g[i][1])
                up = n-(left+right+1)
            else:
                left = get_size(g[i][0])
                right = 0
                up = n-(left+right+1)
            if up==0: up=1
            if left==0: left=1
            if right==0: right=1

            di[left*right*up]+=1
        return di[max(di)]


class Solution2:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def get_size(i):
            if dp[i]!=-1: return dp[i]
            ans = 1 # the node itself
            for child in g[i]: # at max two children
                ans += get_size(child)
            dp[i]=ans
            return dp[i]


        n = len(parents)
        dp = [-1]*n
        g = defaultdict(list)
        for child, par in enumerate(parents): # make graph similar to a tree. no edges to the parent. only edges to the children
            if par==-1: continue
            g[par].append(child)

        di = Counter()
        for i in range(n):
            p = 1 # product
            s = 0 # sum
            for child in g[i]:
                size_child = get_size(child)
                s += size_child
                p *= size_child if size_child != 0 else 1
            up = n-s-1
            p *= up if up != 0 else 1
            di[p]+=1
        return di[max(di)]

class MyTestCase(unittest.TestCase):
    def test1(self):
        parents = [-1,2,0,2,0]
        Output= 3
        self.assertEqual(Output, get_sol().countHighestScoreNodes(parents))
    def test2(self):
        parents = [-1,2,0]
        Output= 2
        self.assertEqual(Output, get_sol().countHighestScoreNodes(parents))
    def test3(self):
        parents = [-1,3,3,5,7,6,0,0]
        Output= 2
        self.assertEqual(Output, get_sol().countHighestScoreNodes(parents))
    # def test4(self):
    # def test5(self):
    # def test6(self):

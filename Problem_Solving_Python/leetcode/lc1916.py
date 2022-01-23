from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1300085/n!-(cnt_0-*-cnt_1-*-..-*-cnt_n-1)
    # extension of -> https://math.stackexchange.com/questions/2982436/spider-problem-counting-socks-and-shoes
    # https://codeforces.com/blog/entry/75627
    def waysToBuildRooms(self, pr: List[int]) -> int:
        mod=10**9+7
        def dfs(u):
            nonlocal prod
            total_cnt=1
            for v in graph[u]:
                total_cnt+=dfs(v)
            prod = prod * total_cnt % mod # update globally
            return total_cnt
        def modPow(x,y,m):
            if y==0:
                return 1
            p = modPow(x,y//2,m)%m
            p = (p*p)%m
            return (p*x)%m if y%2 else p

        graph=[[] for _ in range(len(pr))] # this graph will be a tree
        fact=1
        prod=1
        for i in range(1,len(pr)):
            graph[pr[i]].append(i)
            fact=fact*(i+1)%mod
        dfs(0)
        return fact * modPow(prod,mod-2,mod)%mod # why mod-2 -> https://cp-algorithms.com/algebra/module-inverse.html -> multiply with multiplicative inverse instead of division
class Solution2:
    def waysToBuildRooms(self, pr: List[int]) -> int:
        mod=10**9+7
        def dfs(cur):
            nonlocal prod
            total_cnt=1
            for next in al[cur]:
                total_cnt+=dfs(next)
            prod = prod * total_cnt % mod
            return total_cnt if cur!=0 else prod
        def modPow(x,y,m):
            if y==0:
                return 1
            p = modPow(x,y//2,m)%m
            p = (p*p)%m
            return (p*x)%m if y%2 else p

        al=[[] for _ in range(len(pr))]
        fact=1
        prod=1
        for i in range(1,len(pr)):
            al[pr[i]].append(i)
            fact=fact*(i+1)%mod
        return fact * modPow(dfs(0),mod-2,mod)%mod

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, get_sol().waysToBuildRooms([-1,0,1]))
    def test_2(self):
        self.assertEqual(6, get_sol().waysToBuildRooms([-1,0,0,1,2]))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    #

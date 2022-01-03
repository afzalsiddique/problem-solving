import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # time: O(n)
    # https://leetcode.com/problems/jump-game-v/discuss/498379/Python-concise-actual-O(n)-(monotone-stacks-%2B-DFS)-(also-188ms-beats-100)
    def maxJumps(self, A: List[int], d: int) -> int:
        def f(iterable):
            st=[] # decreasing stack
            for i in iterable:
                while st and A[st[-1]]<A[i]:
                    j=st.pop()
                    if abs(i-j)<=d:
                        g[i].append(j)
                st.append(i)

        @functools.lru_cache(None)
        def jump(i:int):
            res=0
            for j in g[i]:
                res=max(res,jump(j))
            return res+1

        g=defaultdict(list)
        n=len(A)
        f(range(n))
        f(reversed(range(n)))
        res=0
        for i in range(n):
            res=max(res,jump(i))
        return res
class Solution2:
    # time O(n*d)
    def maxJumps(self, arr: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def dfs(i: int):
            li=[] # indices where jump is valid
            prev=float('-inf')
            for k in range(i - 1, max(0, i - d) - 1, -1):
                if arr[k]<arr[i] and arr[k]>=prev:
                    li.append(k)
                prev=max(prev,arr[k])
            prev=float('-inf')
            for k in range(i + 1, min(n, i + d + 1)):
                if arr[k]<arr[i] and arr[k]>=prev:
                    li.append(k)
                prev=max(prev,arr[k])
            res=0
            while li:
                newPos=li.pop()
                res=max(res, dfs(newPos))
            return res+1

        n=len(arr)
        res=0
        for i in range(n):
            res=max(res, dfs(i))
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, get_sol().maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
    def test2(self):
        self.assertEqual(1, get_sol().maxJumps([3,3,3,3,3], 3))
    def test3(self):
        self.assertEqual(7, get_sol().maxJumps([7,6,5,4,3,2,1], 1))
    def test4(self):
        self.assertEqual(3, get_sol().maxJumps([100,96,96,37,37], 4))
    def test5(self):
        self.assertEqual(12, get_sol().maxJumps([83,11,83,70,75,45,96,11,80,75,67,83,6,51,71,64,64,42,70,23,11,24,95,65,1,54,31,50,18,16,11,86,2,48,37,34,65,67,4,17,33,70,16,73,57,96,30,26,56,1,16,74,82,77,82,62,32,90,94,33,58,23,23,65,70,12,85,27,38,100,93,49,96,96,77,37,69,71,62,34,4,14,25,37,70,3,67,88,20,30], 29))
    def test6(self):
        self.assertEqual(4, get_sol().maxJumps([92,85,45,85,37,39], 5))
    def test7(self):
        self.assertEqual(10, get_sol().maxJumps([79,50,41,88,35,29,69,73,59,73,84,21,43,32,25,14,5,60,48,80,86,40,30,7,80,94,32,12,20,39,92,41,85,45,85,84,65,53,6,37,39,52,49,84,64,57,81,38,20,45,43,23,35,78,95,29,66,22,30,23,40,37,76,66,12,84,67,59,82,35,53,25,95,75,81,39,95,83,38,39,15,31,53,30,31,98,67,25,66,4,88,89,10,50,3,12,21,32,88,58,62,69,25,91,78,94,41,11,9,38,49,27,90,37,17,56,30,72,28,99,68,22,75,87,10,59,84,43,81,77], 8))
    def test8(self):
        self.assertEqual(2, get_sol().maxJumps([1,1,1,1,1,2,2,2,2,2],10))

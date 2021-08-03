import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # all length==n strings are at the last level
    # Break when the first string in the queue is length n and find the kth value in the queue.
    def getHappyString(self, n: int, k: int) -> str:
        q=deque(['a','b','c'])
        while len(q[0])!=n:
            for _ in range(len(q)):
                cur=q.popleft()
                for child in 'abc':
                    if cur[-1]==child: continue
                    q.append(cur+child)
        if len(q)>=k:
            return q[k-1]
        return ""
class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(cur):
            if len(cur)==n+1:
                self.left-=1
                if self.left==0:
                    self.res=cur[1:]
            for child in g[cur]:
                dfs(child)

        self.left=k
        self.res=[]
        g=defaultdict(list)
        q=deque(['#'])
        tmp=n
        while q:
            if not tmp: break
            for _ in range(len(q)):
                cur = q.popleft()
                for child in 'abc':
                    if cur[-1]==child: continue
                    q.append(cur+child)
                    g[cur].append(cur+child)
            tmp-=1

        dfs('#')
        return ''.join(self.res)

class Tester(unittest.TestCase):
    def test1(self):
        n = 1; k = 3
        Output= "c"
        self.assertEqual(Output,get_sol().getHappyString(n,k))
    def test2(self):
        n = 1; k = 4
        Output= ""
        self.assertEqual(Output,get_sol().getHappyString(n,k))
    def test3(self):
        n = 3; k = 9
        Output= "cab"
        self.assertEqual(Output,get_sol().getHappyString(n,k))
    def test4(self):
        n = 2; k = 7
        Output= ""
        self.assertEqual(Output,get_sol().getHappyString(n,k))
    def test5(self):
        n = 10; k = 100
        Output= "abacbabacb"
        self.assertEqual(Output,get_sol().getHappyString(n,k))
    # def test6(self):
    # def test7(self):
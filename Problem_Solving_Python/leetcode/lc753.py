import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(path): # make dfs return boolean for optimization. otherwise tle
            nonlocal res
            if len(vis)==total:
                res=path
                return True

            for i in range(k):
                new_path = ''.join(path[-(n - 1):]) + str(i) if n != 1 else str(i)
                if new_path not in vis:
                    vis.add(new_path)
                    if dfs(path + [str(i)]): return True
                    vis.remove(new_path)
            return False

        total = k**n
        vis={"0" * n}
        path = ["0" for _ in range(n)]
        res=[]
        dfs(path)
        return ''.join(res)
class Solution2:
    # tle
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(path):
            nonlocal res
            if len(vis)==total:
                res=path
                return

            for i in range(k):
                new_path = ''.join(path[-(n - 1):]) + str(i) if n != 1 else str(i)
                if new_path not in vis:
                    vis.add(new_path)
                    dfs(path + [str(i)])
                    vis.remove(new_path)
            return

        total = k**n
        vis={"0" * n}
        path = ["0" for _ in range(n)]
        res=[]
        dfs(path)
        return ''.join(res)
class tester(unittest.TestCase):
    def test1(self):
        Output= "01"
        self.assertEqual(Output,get_sol().crackSafe(n = 1, k = 2))
    def test2(self):
        Output= "00110"
        self.assertEqual(Output,get_sol().crackSafe(n = 2, k = 2))
    def test3(self):
        Output= "0001011100"
        self.assertEqual(Output,get_sol().crackSafe(n=3,k=2)   )
    def test4(self):
        Output= "012"
        self.assertEqual(Output,get_sol().crackSafe(n=1,k=3)   )
    def test5(self):
        Output= "00102030411213142232433440"
        self.assertEqual(Output,get_sol().crackSafe(2, 5)   )

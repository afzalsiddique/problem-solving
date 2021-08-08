import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/loud-and-rich/discuss/137918/C%2B%2BJavaPython-Concise-DFS
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(i):
            if res[i]!=-1 and res[i]!=i: return res[i]
            for j in g[i]:
                tmp = dfs(j)
                if quiet[tmp]<quiet[res[i]]:
                    res[i]=tmp
            return res[i]

        n=len(quiet)
        g=defaultdict(list)
        for u,v in richer: g[v].append(u)
        res=[i for i in range(n)]
        for i in range(n): dfs(i)
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        richer,quiet= [[1,0],[2,1],[3,1]], [3,2,5,4]
        Output= [1,1,2,3]
        self.assertEqual(Output,get_sol().loudAndRich(richer,quiet))
    def test_2(self):
        richer,quiet = [],[0]
        Output= [0]
        self.assertEqual(Output,get_sol().loudAndRich(richer,quiet))
    def test_3(self):
        richer,quiet= [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]
        Output= [5,5,2,5,4,5,6,7]
        self.assertEqual(Output,get_sol().loudAndRich(richer,quiet))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
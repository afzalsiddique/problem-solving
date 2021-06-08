import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        rev_graph = [[]*n for _ in range(n)]
        for i in range(n):
            if manager[i]==-1: continue
            rev_graph[manager[i]].append(i)

        self.maxx=0
        def dfs(i,time):
            for neigh in rev_graph[i]:
                dfs(neigh,time+informTime[i])
            self.maxx = max(self.maxx,time+informTime[i])

        dfs(headID,0)
        return self.maxx

class tester(unittest.TestCase):
    def test01(self):
        n = 1
        headID = 0
        manager = [-1]
        informTime = [0]
        Output= 0
        self.assertEqual(Output,get_sol().numOfMinutes(n, headID, manager, informTime))
    def test02(self):
        n = 6
        headID = 2
        manager = [2,2,-1,2,2,2]
        informTime = [0,0,1,0,0,0]
        Output= 1
        self.assertEqual(Output,get_sol().numOfMinutes(n, headID, manager, informTime))
    def test03(self):
        n = 7
        headID = 6
        manager = [1,2,3,4,5,6,-1]
        informTime = [0,6,5,4,3,2,1]
        Output= 21
        self.assertEqual(Output,get_sol().numOfMinutes(n, headID, manager, informTime))
    def test04(self):
        n = 15
        headID = 0
        manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
        informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        Output= 3
        self.assertEqual(Output,get_sol().numOfMinutes(n, headID, manager, informTime))
    def test05(self):
        n = 4
        headID = 2
        manager = [3,3,-1,2]
        informTime = [0,0,162,914]
        Output= 1076
        self.assertEqual(Output,get_sol().numOfMinutes(n, headID, manager, informTime))
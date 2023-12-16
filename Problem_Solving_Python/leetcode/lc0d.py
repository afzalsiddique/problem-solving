from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        NOT_VISITED,VISITING,VISITED=-1,0,1
        def dfs(i):
            if visits[i]==VISITED:
                return True
            if visits[i]==VISITING:
                return False
            visits[i]=VISITING
            for j in g[i]:
                if not dfs(j): return False
            visits[i]=VISITED
            return True

        g=defaultdict(list)
        for a,b in prerequisites: g[b].append(a)
        visits=[NOT_VISITED]*numCourses
        for i in range(numCourses):
            dfs(i)
        return all(visits[i]==1 for i in range(numCourses))




class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True,get_sol().canFinish(2,[[1,0]]))
    def test2(self):
        self.assertEqual(False,get_sol().canFinish(2,[[1,0],[0,1]]))
    def test3(self):
        self.assertEqual(True,get_sol().canFinish(1, []))
    def test4(self):
        self.assertEqual(True,get_sol().canFinish(2, []))
    def test5(self):
        self.assertEqual(True,get_sol().canFinish(4, [[0,3],[1,3],[2,0],[2,1]]))
    def test6(self):
        self.assertEqual(True,get_sol().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
    # def test7(self):

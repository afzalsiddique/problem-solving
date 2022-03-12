from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path[:])
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([[0,1,3],[0,2,3]], get_sol().allPathsSourceTarget([[1, 2], [3], [3], []]))
    def test02(self):
        self.assertEqual([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], get_sol().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))

from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# cycle detection using dfs
# time O(n^2) space O(n)
class Solution:
    # https://www.youtube.com/watch?v=dB8JV5UvpBM
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)

        # if target is reachable from src
        def dfs(src,target,visited):
            if src in visited: return False
            if src == target: return True # target is reachable
            visited.addInReverse(src)
            for neigh in graph[src]:
                if dfs(neigh,target,visited):
                    return True
            return False

        for src,target in edges:
            if dfs(src,target,set()): # if adding this edge forms cycle return this edge
                return [src,target]
            # if it does not form cycle then add it to the graph
            graph[src].append(target)
            graph[target].append(src)

class tester(unittest.TestCase):
    def test1(self):
        input = [[1,2], [1,3], [2,3]]
        Output= [2,3]
        self.assertEqual(Output,get_sol().findRedundantConnection(input))
    def test2(self):
        input = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        Output= [1,4]
        self.assertEqual(Output,get_sol().findRedundantConnection(input))

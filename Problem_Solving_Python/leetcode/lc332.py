from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)

        for src in graph:
            graph[src].sort(reverse=True) # https://www.youtube.com/watch?v=WYqsg5dziaQ&t=392s
            # graph[src].sort() # this will also work if we pop items from the left

        stack = ['JFK']
        res = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
                # stack.append(graph[stack[-1]].pop(0)) # this will work if sorted in lexicographical order
            else:
                res.append(stack.pop())
        return res[::-1]
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(u, i): # i-> ticket index
            if i in vis:
                return []
            vis.add(i)
            if len(vis)==len(tickets):
                return [u]
            res=[u]
            for v,idx in g[u]:
                path= dfs(v, idx)
                if path:
                    res.extend(path)
                    return res
            vis.remove(i)
            return []

        g=defaultdict(list)
        for i,(a,b) in enumerate(tickets): # i-> ticket index
            g[a].append((b,i))
        for x in g:
            g[x].sort()

        for v,i in g['JFK']:
            vis=set()
            path= dfs(v, i)
            if path:
                return ['JFK']+path
        return []
class tester(unittest.TestCase):
    def test3(self):
        # https://www.youtube.com/watch?v=8MpoO2zA2l4&t=254s
        tickets = [["JFK","1"],["1","2"],["2","1"],["1","3"],["3","4"]]
        Output= ['JFK','1','2','1','3','4']
        self.assertEqual(Output,get_sol().findItinerary(tickets))
    def test1(self):
        tickets = [["0","1"],["JFK","0"],["2","3"],["1","2"]]
        Output= ["JFK","0","1","2","3"]
        self.assertEqual(Output,get_sol().findItinerary(tickets))
    def test2(self):
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output= ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(Output,get_sol().findItinerary(tickets))

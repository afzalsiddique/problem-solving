import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


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

class tester(unittest.TestCase):
    def test3(self):
        # https://www.youtube.com/watch?v=8MpoO2zA2l4&t=254s
        tickets = [["JFK","1"],["1","2"],["2","1"],["1","3"],["3","4"]]
        Output= ['JFK','1','2','1','3','4']
        self.assertEqual(Output,Solution().findItinerary(tickets))
    def test1(self):
        tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        Output= ["JFK","MUC","LHR","SFO","SJC"]
        self.assertEqual(Output,Solution().findItinerary(tickets))
    def test2(self):
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output= ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(Output,Solution().findItinerary(tickets))

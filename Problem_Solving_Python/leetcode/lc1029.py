from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # time O(nlogn)
    # https://leetcode.com/problems/two-city-scheduling/discuss/667786/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs)//2
        minCost = 0
        for a, b in costs:
            refund.append(b - a)
            minCost += a # buy everyone a ticket to city a
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost

class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        costs.sort(key=lambda x:x[0]-x[1])
        res=0
        for i in range(n//2):
            res+=costs[i][0]
        for i in range(n//2,n):
            res+=costs[i][1]
        return res
class Solution3:
    # time O(n^2)
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        a=b=n//2
        dp={}
        def helper(i,a,b):
            if i==n: return 0
            if (i,a,b) in dp: return dp[(i,a,b)]
            option1,option2=float('inf'),float('inf')
            if a and b:
                option1 = costs[i][0]+helper(i+1,a-1,b)
                option2 = costs[i][1]+helper(i+1,a,b-1)
            elif a:
                option1 = costs[i][0]+helper(i+1,a-1,b)
            elif b:
                option1 = costs[i][1]+helper(i+1,a,b-1)
            dp[(i,a,b)] = min(option1,option2)
            return dp[(i,a,b)]

        return helper(0,a,b)


class tester(unittest.TestCase):
    def test1(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        Output= 110
        self.assertEqual(Output, get_sol().twoCitySchedCost(costs))
    def test2(self):
        costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        Output= 1859
        self.assertEqual(Output, get_sol().twoCitySchedCost(costs))
    def test3(self):
        costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        Output= 3086
        self.assertEqual(Output, get_sol().twoCitySchedCost(costs))

import unittest
from collections import deque
from typing import List

from typing import List

# time O(nlogn)
class Solution:
    # https://leetcode.com/problems/two-city-scheduling/discuss/667786/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs)//2
        minCost = 0
        for A, B in costs:
            refund.append(B - A)
            minCost += A
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost

# time O(n^2)
class Solution2:
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


def get_sol_obj(): return Solution()
class tester(unittest.TestCase):
    def test1(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        Output= 110
        self.assertEqual(Output,get_sol_obj().twoCitySchedCost(costs))
    def test2(self):
        costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        Output= 1859
        self.assertEqual(Output,get_sol_obj().twoCitySchedCost(costs))
    def test3(self):
        costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        Output= 3086
        self.assertEqual(Output,get_sol_obj().twoCitySchedCost(costs))

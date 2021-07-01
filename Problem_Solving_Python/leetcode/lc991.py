import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/broken-calculator/discuss/1076046/Python-Greedy-solution-explained
    # greedy
    # start from y and try to reach x
    def brokenCalc(self, x: int, y: int) -> int:
        def helper(x,y):
            if y==x: return 0
            if y<x: # no need to divide
                return x-y
            elif y%2==0:
                return 1+helper(x,y//2)
            else:
                return 1+helper(x,y+1)

        return helper(x,y)
class Solution2:
    # wrong. dfs gets stuck in infinite function call
    def brokenCalc(self, x: int, y: int) -> int:
        dp = {}
        def dfs(y):
            print(y)
            if y==x:
                return 1
            if y==0: return float('inf')
            if y in dp: return dp[y]
            if y<x:
                dp[y]=1+dfs(y+1)
            else:
                dp[y]=1+min(dfs(y//2),dfs(y+1))
            return dp[y]

        return dfs(y)

class tester(unittest.TestCase):
    def test01(self):
        x = 2
        y = 3
        Output= 2
        self.assertEqual(Output,get_sol().brokenCalc(x,y))
    def test02(self):
        x = 5
        y = 8
        Output= 2
        self.assertEqual(Output,get_sol().brokenCalc(x,y))
    def test03(self):
        x = 3
        y = 10
        Output= 3
        self.assertEqual(Output,get_sol().brokenCalc(x,y))
    def test04(self):
        x = 1024
        y = 1
        Output= 1023
        self.assertEqual(Output,get_sol().brokenCalc(x,y))
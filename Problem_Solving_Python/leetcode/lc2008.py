import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # same as 1235 except we need to update tip to profit
    # dp denotes maximum profit when considering items[0 .... i]
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides = [[s,e,e-s+t] for s,e,t in rides] # update tip to make this points/profits. only this line is different from leetcode 1235
        begin, end, profit = zip(*sorted(rides, key=lambda x:x[1]))

        dp = [p for p in profit]
        for i in range(len(rides)):
            if i==0: continue # there is no item before this. so merging is not possible
            option1,option2 = float('-inf'),float('-inf')
            # find largest end[j] value in the array end where end[j]<=begin[i]
            j = bisect_right(end, begin[i])
            if end[j]>begin[i]:
                j-=1
            if j>=0: # if taking both of the items possible
                option1 = dp[j]+profit[i]
            option2 = dp[i-1]# maximum profit from items[0 ... i-1]
            dp[i] = max(dp[i],option1,option2) # maximum profit from items[0 ... i]

        return dp[-1]

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,rides = 5,  [[2,5,4],[1,5,1]]
        Output= 7
        self.assertEqual(Output, get_sol().maxTaxiEarnings(n,rides))
    def test2(self):
        n,rides = 20,  [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
        Output= 20
        self.assertEqual(Output, get_sol().maxTaxiEarnings(n,rides))
    def test3(self):
        n,rides = 10, [[4,5,8],[3,6,6],[1,3,3],[2,5,9],[4,9,5],[8,9,10],[3,8,5],[3,5,2],[3,7,10],[9,10,6]]
        Output= 37
        self.assertEqual(Output, get_sol().maxTaxiEarnings(n,rides))
    # def test4(self):
    # def test5(self):
    # def test6(self):

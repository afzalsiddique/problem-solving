import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=ZYsuW19NMeo
class Solution:
    # dp denotes maximum profit when considering items[0 .... i]
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit), key=lambda x:x[1]))

        dp = [p for p in profit]
        for i in range(n):
            if i==0: continue # there is no item before this. so merging is not possible
            option1,option2 = float('-inf'),float('-inf')
            # find largest end[j] value in the array end where end[j]<=start[i]
            j = bisect_right(end, start[i])
            j-=1
            if j>=0: # if taking both of the items possible
                option1 = dp[j]+profit[i]
            option2 = dp[i-1] # maximum profit considering items[0 ... i-1]
            dp[i] = max(dp[i],option1,option2) # maximum profit considering items[0 ... i]

        return dp[-1]

class Solution2:
    # dp denotes maximum profit when considering items[i+1 .... n-1]
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        n=len(start)
        dp = [profit[i] for i in range(n)]
        for i in reversed(range(n)):
            option1,option2 = float('-inf'),float('-inf')
            if i==n-1:continue # there is no item after this. so merging is not possible
            # find smallest start[j] where start[j]>=end[i]
            j = bisect_left(start, end[i])
            if j!=n: # if taking both items is possible
                option1 = dp[j]+profit[i]
            option2 = dp[i+1]  # maximum profit considering items[i+1 ... n-1]
            dp[i] = max(dp[i],option1,option2) # maximum profit considering items[i ... n-1]
        return dp[0]

class Solution3:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))

        dp = [0 for _ in range(n + 1)]
        for i in reversed(range(n)):
            j = bisect_left(start, end[i])
            # j = bisect_left(start, end[i],lo=i+1) # optimization. searching only on the right side of i is enough
            dp[i] = max(dp[i + 1],  dp[j]+profit[i])

        return dp[0]

class Solution4:
    #  TLE. O(n^^2)
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start,end,profit = zip(*sorted(zip(start,end,profit)))
        dp = [p for p in profit]
        for i in reversed(range(n)):
            for j in reversed(range(i+1,n)):
                if end[i]<=start[j]:
                    dp[i]=max(dp[i]+dp[j]+profit[i])
        return max(dp)
class MyTestCase(unittest.TestCase):
    def test1(self):
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 4]
        profit = [50, 10, 40, 70]
        expected = 120
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))
    def test2(self):
        startTime = [1,2,3,4,6]
        endTime = [3,5,10,6,9]
        profit = [20,20,100,70,60]
        expected = 150
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))
    def test3(self):
        startTime = [1,1,1]
        endTime = [2,3,4]
        profit = [5,6,4]
        expected = 6
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))
    def test4(self):
        startTime = [1,2,2,3]
        endTime = [2,5,3,4]
        profit = [3,4,1,2]
        expected = 7
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))
    def test5(self):
        startTime = [4,2,4,8,2]
        endTime = [5,5,5,10,8]
        profit = [1,2,8,10,4]
        expected = 18
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))
    def test6(self):
        startTime = [6,15,7,11,1,3,16,2]
        endTime = [19,18,19,16,10,8,19,8]
        profit = [2,9,1,19,5,7,3,19]
        expected = 41
        self.assertEqual(expected, get_sol().jobScheduling(startTime, endTime,profit))

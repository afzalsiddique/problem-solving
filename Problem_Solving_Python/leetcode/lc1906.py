import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # tle
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if abs(nums[j]-nums[i])==0:
                    dp[i][j]= min(dp[i+1][j],dp[i][j-1])
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1],abs(nums[j]-nums[i]))
        # for x in dp: print(x)
        res = []
        for l,r in queries:
            tmp = dp[l][r]
            res.append(tmp if tmp != float('inf') else -1)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,queries = [1,3,4,8],  [[0,1],[1,2],[2,3],[0,3]]
        Output= [2,1,4,1]
        self.assertEqual(Output, get_sol().minDifference(nums,queries))
    def test2(self):
        nums,queries = [4,5,2,2,7,10],  [[2,3],[0,2],[0,5],[3,5]]
        Output= [-1,1,1,3]
        self.assertEqual(Output, get_sol().minDifference(nums,queries))
    def test3(self):
        nums,queries = [10,6,10,4,2], [[0,2],[2,3],[1,2],[3,4],[3,4]]
        Output= [4,6,4,2,2]
        self.assertEqual(Output, get_sol().minDifference(nums,queries))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

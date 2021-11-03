import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/1028098/Java-Recursive-to-Memoization-to-DP
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp={}
        def h(i):
            if i==n: return 0
            if i in dp: return dp[i]
            cur_max=0
            sum_max=0
            for j in range(k):
                to=i+j
                if to==n: break
                cur_max=max(cur_max,arr[to])
                left=cur_max*(j+1)
                right=h(to+1)
                sum_max=max(sum_max,left+right)
            dp[i]=sum_max
            return sum_max

        return h(0)

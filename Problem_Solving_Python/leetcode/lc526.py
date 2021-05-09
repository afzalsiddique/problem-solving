import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

# bit masking
class Solution:
    # https://leetcode.com/problems/beautiful-arrangement/discuss/1000132/Python-DP-%2B-bitmasks-explained
    def countArrangement(self, N):
        dp = {}
        def dfs(mask, i):
            if i == 0: return 1
            if (mask, i) in dp: return dp[(mask, i)]
            total = 0
            for num in range(N):
                if not mask & 1 << num and ((num + 1) % i == 0 or i % (num + 1) == 0):
                    total += dfs(mask ^ 1 << num, i - 1)
            dp[(mask, i)]=total
            return total

        return dfs(0, N)


class Solution2:
    def countArrangement(self, N: int) -> int:
        dp={}
        def helper(i, tup):
            if i==0: return 1
            key=(i, tup)
            if key in dp: return dp[key]
            total=0
            for j in range(len(tup)):
                if tup[j]%i==0 or i%tup[j]==0:
                    total+=helper(i - 1, tup[:j] + tup[j + 1:])
            dp[key]=total
            return total
        tup=tuple(i for i in range(1,N+1))
        return helper(N,tup)

# tle
class Solution3:
    def countArrangement(self, N: int) -> int:
        all_permutations=[]
        nums = [i for i in range(1,N+1)]
        def permute(start,path):
            if start==len(nums):
                all_permutations.append(path)
                return
            for i in range(start,len(nums)):
                permute(i,path+[nums[i]])
        def check_if_beautiful(nums):
            for i in range(len(nums)):
                idx=i+1
                if nums[i]%idx==0 or idx%nums[i]==0: continue
                else: return False
            return True
        permute(nums, [])
        ans=0
        for nums in all_permutations:
            if check_if_beautiful(nums):
                ans+=1
        return ans

class tester(unittest.TestCase):
    def test1(self):
        n = 2
        Output= 2
        self.assertEqual(Output,get_sol().countArrangement(n))
    def test2(self):
        n = 1
        Output= 1
        self.assertEqual(Output,get_sol().countArrangement(n))
    def test3(self):
        n = 4
        Output= 8
        self.assertEqual(Output,get_sol().countArrangement(n))

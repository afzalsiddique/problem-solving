from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    # https://www.youtube.com/watch?v=hqGa65Rp5LQ
    # https://www.youtube.com/watch?v=MqYLmIzl8sQ
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summ = sum(nums)
        if summ < S or (summ + S) % 2 == 1:
            return 0
        target = (sum(nums)+S) // 2
        return self.sumSubset(nums, target)
    def sumSubset(self, nums, target):
        n = len(nums)
        nums = ['#'] + nums
        dp = [[0]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,target+1):
                if j<nums[i] or nums[i] == 0: # if nums[i]==0:skip it
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]
        zeros = 0
        for num in nums:
            if num==0:zeros+=1
        return int(2**zeros) * dp[-1][-1] # see below for explanation

# For those who has problem with test case  [0,0,0,0,0,0,0,0,1], target = 1.
# According to Mazhar Imam Khan,
# The solution doesn't consider presence of "0"s in the array. Why the output is different ?
# Because, if we have "0", then, it can have +0 and -0 and still will not effect the sum of a set. For example: Target value is = 2
# 1) {0,2} = {+0,2}, {-0,2}.  Ans: 2
# But if we increase number of 0s,
# 2) {0,0,2} = {+0,+0,2}, {+0,-0,2}, {-0,+0,2},{-0,-0,2} . Ans: 4
#
# So, if you observe, your answer increase by (2^number of 0s) i.e. pow(2,number of zeros).
# So, make a small change as follows:
# 1) on count of subsetsum function,
# if(nums[i-1] > j )    => change to:  if (nums[i-1] > j || nums[i-1] == 0)
#       dp[i][j] = dp[i-1][j];
#  //make no change and put the previous value as it is in the next subproblem. (I.e. 2, in example above)
# And then at the end, you answer will be
# return (int)Math.pow(2, number of 0s) * dp[nums.length][target] ;
#
# Also, other cases we need to handle is:
# if (S > sum || (sum + S) % 2 != 0){ //S is target
#             return 0;

# i don't know why this code below works :(
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summ = sum(nums)
        if summ < S or (summ + S) % 2 == 1:
            return 0
        target = (sum(nums)+S) // 2
        return self.sumSubset(nums, target)
    def sumSubset(self, nums, target):
        n = len(nums)
        nums = ['#'] + nums
        dp = [[0]*(target+1) for _ in range(n+1)]
        # for i in range(n+1): ## changes here
        #     dp[i][0] = 1
        dp[0][0] = 1 ## changes here
        for i in range(1,n+1):
            for j in range(0,target+1):
                if j>=nums[i]: ## changes here
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        zeros = 0
        for num in nums:
            if num==0:zeros+=1
        # return int(2**zeros) * dp[-1][-1] ## changes here
        return dp[-1][-1] ## changes here

class Solution3:
    # TLE. time complexity 2^n
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        def dfs(i,target):
            if i==n:
                if target==0: return 1
                return 0
            else:
                return  dfs(i+1, target-nums[i]) + dfs(i+1,target+nums[i])

        return dfs(0,S)

class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,Solution().sumSubset([1,2,1],3))
    def test2(self):
        self.assertEqual(0,Solution().findTargetSumWays([1],2))
    def test3(self):
        self.assertEqual(256,Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
    def test4(self):
        self.assertEqual(2,Solution().findTargetSumWays([1,0],1))
    def test5(self):
        self.assertEqual(792,Solution().findTargetSumWays([1,1,1,1,1,1,1,1,1,1,1,1],2))

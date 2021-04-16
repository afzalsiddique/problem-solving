import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    # https://leetcode.com/problems/wiggle-subsequence/discuss/84843/Easy-understanding-DP-solution-with-O(n)-Java-version/89522
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        up,down=1,1
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                down=up+1
            elif nums[i]>nums[i-1]:
                up=down+1
        return max(up,down)

class Solution2:
    # https://leetcode.com/problems/wiggle-subsequence/discuss/84843/Easy-understanding-DP-solution-with-O(n)-Java-version
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # dp[i][0] is the length of sequence ending at i and the last before element is lesser than last element. Eg. [9 2 5]
        # dp[i][1] is the length of sequence ending at i and the last before element is greater than last element. Eg. [2 10 5]
        n=len(nums)
        dp=[[1]*2 for _ in range(n)]
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                dp[i][0]=max(dp[i][0],1+dp[i-1][1])
                dp[i][1]=dp[i-1][1]
            elif nums[i]>nums[i-1]:
                dp[i][1]=max(dp[i][1],1+dp[i-1][0])
                dp[i][0]=dp[i-1][0]
            else:
                dp[i][1]=dp[i-1][1]
                dp[i][0]=dp[i-1][0]
        # return max(max(dp)) # this is wrong
        return max(map(max,dp))

# similar longest increasing subsequence
class Solution3:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # dp[i][0] is the length of sequence ending at i and the last before element is lesser than last element. Eg. [9 2 5]
        # dp[i][1] is the length of sequence ending at i and the last before element is greater than last element. Eg. [2 10 5]
        n=len(nums)
        dp=[[1]*2 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i]<nums[j]:
                    dp[i][0]=max(dp[i][0],1+dp[j][1])
                elif nums[i]>nums[j]:
                    dp[i][1]=max(dp[i][1],1+dp[j][0])
                else: # not necessary in this method but useful when doing it in O(n) time and O(n) space
                    dp[i][0]=max(dp[i][0],1)
                    dp[i][1]=max(dp[i][1],1)

        # return max(max(dp)) # this is wrong
        return max(map(max,dp))
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(7,Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    def test2(self):
        self.assertEqual(3,Solution().wiggleMaxLength([3,3,3,2,5]))

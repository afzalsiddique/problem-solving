from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

# greedy
class Solution4:
    # https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution/237098
    # start position from the end
    # Find the leftmost position that can reach the current position.
    def jump(self, nums: List[int]) -> int:
        position = len(nums)-1
        steps=0
        while position:
            for i in range(position):
                if nums[i]+i>=position:
                    position=i
                    steps+=1
                    break
        return steps
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        def helper(position):
            if position>=n-1:return 0
            if dp[position]!=-1:return dp[position]
            farthest = nums[position]+position
            minn = float('inf')
            for i in range(position+1, farthest+1):
                minn = min(minn, helper(i))
            dp[position]=1+minn
            return dp[position]

        return helper(0)

class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(position):
            if position>=n-1:return 0
            farthest = nums[position]+position
            minn = float('inf')
            for i in range(position+1, farthest+1):
                minn = min(minn, helper(i))
            return 1+minn

        return helper(0)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(2, Solution().jump([2,3,1,1,4]))
    def test_2(self):
        self.assertEqual(2, Solution().jump([2,3,0,1,4]))
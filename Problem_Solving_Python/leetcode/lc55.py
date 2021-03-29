from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
# greedy
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        max_reached = 0
        n = len(nums)
        for i in range(n):
            if i>max_reached:return False
            max_reached = max(max_reached, nums[i]+i)
        return True

# bottom up dp. tle
class Solution4:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1]*n
        def canjumpfromposition(position):
            if position>=n-1:
                return True
            if dp[position]!=-1:return dp[position]
            farthest = nums[position]+position
            for i in range(position+1, farthest+1):
                if canjumpfromposition(i):
                    dp[position]=True
                    return True
            dp[position]= False
            return False

        return canjumpfromposition(0)

# recursive. TLE
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        def canjumpfromposition(position):
            if position>=n-1:return True
            farthest = nums[position]+position
            for i in range(position+1, farthest+1):
                if canjumpfromposition(i):
                    return True
            return False

        return canjumpfromposition(0)

# dp. from minimum jumps to reach the last index. same code as jump game ii
class Solution:
    # https://www.youtube.com/watch?v=cETfFsSTGJI
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if j+ nums[j]>=i:
                    dp[i] = min(dp[i], dp[j]+1)
        if dp[n-1]==float('inf'):
            return False
        return True

class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, Solution().canJump([2,3,1,1,4]))
    def test_2(self):
        self.assertEqual(False, Solution().canJump([3,2,1,0,4]))
    def test_3(self):
        self.assertEqual(True, Solution().canJump([0]))

    def test_4(self):
        solution = Solution()
        nums = [2,3,1,1,4]
        actual = solution.canJump(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [3,1,0,0,4]
        actual = solution.canJump(nums)
        expected = False
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [0,2,3]
        actual = solution.canJump(nums)
        expected = False
        self.assertEqual(expected, actual)

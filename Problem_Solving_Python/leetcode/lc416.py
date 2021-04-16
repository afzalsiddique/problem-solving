# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973
import unittest
from typing import List


class Solution:
    # iterative
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        nums=[0]+nums
        summ = sum(nums)
        if summ%2:return False
        target=summ//2
        dp=[[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,target+1):
                if j<nums[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]

    # recursive
    def canPartition6(self, nums: List[int]) -> bool:
        n=len(nums)
        di={}
        def helper(start, target):
            if target==0:return True
            if target<0: return False
            if start==n:return False
            if (start, target) in di:return di[(start, target)]
            pick,not_pick=False,False
            for i in range(start,n):
                pick = pick or helper(i+1,target-nums[i])
                if pick:return True
                not_pick = not_pick or helper(i+1,target)
                if not_pick:return True
                di[(start,target)]= pick or not_pick
            return di[(start,target)]

        summ = sum(nums)
        if summ%2:return False
        target=summ//2
        return helper(0,target)


    def canPartition2(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        n = len(nums)
        SUMM = sum(nums) // 2
        numbers = [0]
        for num in nums:
            numbers.append(num) # converting to 1 based indexing
        dp = [[False]*(SUMM+1) for _ in range(n+1)]
        for row in dp:
            row[0] = True
        for i in range(1, n+1):
            for j in range(1, SUMM+1):
                item_not_included = dp[i-1][j]
                if j >= numbers[i] and dp[i-1][j-numbers[i]]:
                    item_included = True
                else:
                    item_included = False
                if item_included or item_not_included:
                    dp[i][j] = True
        return dp[n][SUMM]

    # TLE
    # recursive
    # https://leetcode.com/problems/partition-equal-subset-sum/discuss/90618/7-Lines-59ms-Recursive-Python-Solution/95063
    def canPartition3(self, nums):
        dp = {}
        def helper(start, target):
            if (start, target) in dp:
                return dp[(start, target)]
            elif target == 0:
                return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            dp[(start, target)] = False
            return False

        if max(nums) > sum(nums) // 2:
            return False
        return False if sum(nums)%2 else helper(0, sum(nums)//2)


    # https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
    # https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973
    def canPartition4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_val = sum(nums)
        if sum_val % 2 == 1:
            return False
        target = sum_val // 2
        dp = [False] * (sum_val + 1)
        dp[0] = True
        for i in range(len(nums)):
            next_dp = [False] * (sum_val + 1)
            for j in range(len(dp)):
                if dp[j]:
                    next_dp[j + nums[i]] = True
                    next_dp[j] = True
            dp = next_dp
        return dp[target]
class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [5,4,2,2,4,3]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [1, 5, 11, 5]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [1, 2, 3, 5]
        actual = solution.canPartition(nums)
        expected = False
        self.assertEqual(expected, actual)
    def test4(self):
        self.assertEqual(True, Solution().canPartition([6,4,7,5]))
    def test5(self):
        solution = Solution()
        nums = [1, 1]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

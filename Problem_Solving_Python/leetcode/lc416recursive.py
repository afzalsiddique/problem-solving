# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90618/7-Lines-59ms-Recursive-Python-Solution/95063
class Solution:
    def canPartition(self, nums):
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


def my_func(nums):
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

    return False if sum(nums)%2 else helper(0, sum(nums)//2)
from typing import List


class Solution:
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,path):
            n=len(nums)
            if n==1:
                res.append(path+nums)
                return
            for i in range(n):
                if i>0 and nums[i]==nums[i-1]:continue
                temp = nums[:i]+nums[i+1:8]
                backtrack(temp, path+[nums[i]])

        res = []
        nums.sort()
        backtrack(nums,[])
        return res
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = {}

        def helper(nums):
            n = len(nums)
            if n == 1: return [nums]
            if tuple(nums) in dp: return dp[tuple(nums)]
            result = []
            for i in range(n):
                new_nums = nums[:i] + nums[i + 1:] # remove ith element
                ans = self.permuteUnique(new_nums)
                for item in ans:
                    if [nums[i]] + item not in result:
                        result.append([nums[i]] + item)
            dp[tuple(nums)] = result
            return result

        return helper(nums)

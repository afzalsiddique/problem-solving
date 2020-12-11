# https://www.youtube.com/watch?v=quAS1iydq7U
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        prev = float('-inf')
        i = n-1
        while nums[i] >= prev:
            prev = nums[i]
            i-=1
        a = nums[i]
        j = n-1
        while a > nums[j]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
        nums_copy = nums[:i+1] + nums[-1:i:-1]
        for i in range(n):
            nums[i] = nums_copy[i]
        print(nums_copy)



# from typing import List
#
#
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         dp = {}
#
#         # calculate all possible permutations.
#         def helper(nums):
#             n = len(nums)
#             if n == 1: return [nums]
#             if tuple(nums) in dp: return dp[tuple(nums)]
#             result = []
#             for i in range(n):
#                 new_nums = nums[:i] + nums[i + 1:] # remove ith element
#                 ans = helper(new_nums)
#                 for item in ans:
#                     result.append([nums[i]] + item)
#             dp[tuple(nums)] = result
#             return result
#
#
#         result = sorted(helper(nums))
#         n = len(result)
#         idx = n - result[::-1].index(nums) -1 #find the index of the last occurence
#         if idx != n-1: # if the nums is not the last element
#             for i in range(len(nums)):
#                 nums[i] = result[idx+1][i]
#         else: # if the nums is the last element
#             for i in range(len(nums)):
#                 nums[i] = result[0][i]
#         return
#
#
#
#
#
#
#
#
#

# from typing import List
#
#
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         largest = nums[-1]
#         second_largest_index = -1
#         for i in range(n - 2, -1, -1):
#             if nums[i]<largest:
#                 second_largest_index = i
#                 break
#         if second_largest_index != -1:
#             # swap
#             nums[second_largest_index], nums[second_largest_index+1] = nums[second_largest_index+1], nums[second_largest_index]
#             return
#         nums.sort()
#

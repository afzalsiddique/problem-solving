from bisect import *


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def mybisect_right(A, x):
            # A is a non-increasing
            left, right = 0, len(A)-1
            while left < right:
                mid = (left+right+1)//2 # right mid
                if x <= A[mid]:
                    left = mid
                else:
                    right = mid - 1

            return left

        ans = 0
        for i, x in enumerate(nums1):
            j = mybisect_right(nums2,x)
            ans = max(ans, j-i)

        return ans

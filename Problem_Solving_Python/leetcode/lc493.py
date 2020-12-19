from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def mergeSort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2 + 1
            count = mergeSort(start, mid - 1) + mergeSort(mid, end)
            j = mid
            for i in range(start, mid):
                while j <= end and nums[j] * 2 < nums[i]:
                    j += 1
                count += (j - mid)
            nums[start:end + 1] = sorted(nums[start:end + 1])
            return count

        return mergeSort(0, len(nums) - 1)


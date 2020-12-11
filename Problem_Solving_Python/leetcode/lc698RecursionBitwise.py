from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def selectItem(items, itemNo):
            return items | (1<<itemNo)

        def selected(items, itemNo):
            temp = items & (1<<itemNo)
            if temp==0:
                return False
            return True

        def canPartitionKSubsetsFrom(nums, k, items, targetSubsetSum, curSubsetSum, nextIndexToCheck):
            if k==0:
                return True
            if curSubsetSum == targetSubsetSum:
                return canPartitionKSubsetsFrom(nums, k-1, items, targetSubsetSum, 0, 0)
            for i in range(len(nums)):
                if not selected(items, i) and curSubsetSum + nums[i]<=targetSubsetSum:
                    itemsBeforeSelecting = items
                    items = selectItem(items, i)
                    itmsbin = bin(items)
                    if canPartitionKSubsetsFrom(nums, k, items, targetSubsetSum, curSubsetSum+nums[i], i+1):
                        return True
                    items = itemsBeforeSelecting # backtracking
            return False

        summ = sum(nums)
        maxNum = max(nums)
        if summ % k != 0 or maxNum > summ / k:
            return False

        items = 0
        return canPartitionKSubsetsFrom(nums, k, items, summ//k, 0, 0)



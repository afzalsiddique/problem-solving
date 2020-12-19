from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tsum = sum(nums)
        n = len(nums)

        def go(i, mask, k, csum):
            if k==1:
                return True
            if csum == tsum:
                return go(0, mask, k-1, 0)
            elif csum > tsum:
                return False

            for j in range(i, n):
                if not (mask&(1<<j)):
                    if go(j, mask|(1<<j), k, csum+nums[j]):
                        return True
            return False

        if tsum%k!=0:
            return False
        tsum/=k
        return go(0, 0, k, 0)
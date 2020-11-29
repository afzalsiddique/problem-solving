from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x= len(nums1)
        y = len(nums2)
        if x>y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        low = 0
        high = x
        while True:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            if partitionX==0:
                maxLeftX = float('-inf')
            else:
                maxLeftX = nums1[partitionX - 1]
            if partitionX == x:
                minRightX = float('inf')
            else:
                minRightX = nums1[partitionX]
                
            if partitionY==0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[partitionY - 1]
            if partitionY == y:
                minRightY = float('inf')
            else:
                minRightY = nums2[partitionY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x+y) %2:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
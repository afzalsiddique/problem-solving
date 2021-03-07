# https://www.youtube.com/watch?v=LPFhl65R7ww
import unittest
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):return self.findMedianSortedArrays(nums2,nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        high  = n1 # !!! need to set as n1 and not "n1-1", because this means number of elements on the left side or right side, not the index

        while low<=high:
            partition_x = (low+high)//2
            partition_y = (n1+n2+1)//2-partition_x

            # Why "else float('-inf')" and similarly others?
            # -> Run this case: [1,2,3,4], [5,6,7,8]
            # these are used to satisfy the conditions "maxLeft_x <= minRight_y and maxLeft_y <= minRight_x"
            # -INF 0 1 2 3 4 5 +INF
            # -INF 0 1 2 3 4 5 +INF
            maxLeft_x = nums1[partition_x-1] if partition_x!=0 else float('-inf')
            minRight_x = nums1[partition_x] if partition_x!=n1 else float('inf')

            maxLeft_y = nums2[partition_y-1] if partition_y!=0 else float('-inf')
            minRight_y = nums2[partition_y] if partition_y!=n2 else float('inf')

            if maxLeft_x <= minRight_y and maxLeft_y <= minRight_x:
                if (n1+n2)%2==0:
                    return (max(maxLeft_x,maxLeft_y)+min(minRight_x,minRight_y))/2
                else:
                    return max(maxLeft_x,maxLeft_y)
            elif maxLeft_x > minRight_y:
                high = partition_x-1
            else:
                low = partition_x+1

class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums1 = [1]
        nums2 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 11
        self.assertEqual(expected, actual)
    def test_2(self):
        solution = Solution()
        nums1 = [1,2,3,4]
        nums2 = [5,6,7,8]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 11
        self.assertEqual(expected, actual)
    def test_3(self):
        solution = Solution()
        nums1 = [1,3,8,9,15]
        nums2 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 11
        self.assertEqual(expected, actual)

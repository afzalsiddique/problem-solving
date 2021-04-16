# https://www.youtube.com/watch?v=LPFhl65R7ww
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
            mid1 = (low+high)//2
            mid2 = (n1+n2+1)//2-mid1 # here +1 is for taking one extra element in the left side when n1+n2 is odd

            # Why "else float('-inf')" and similarly others?
            # -> Run this case: [1,2,3,4], [5,6,7,8]
            # these are used to satisfy the conditions "x1 <= y2 and y1 <= x2"
            # -INF 0 1 2 3 4 5 +INF
            # -INF 0 1 2 3 4 5 +INF
            x1 = nums1[mid1-1] if mid1!=0 else float('-inf')
            x2 = nums1[mid1] if mid1!=n1 else float('inf')

            y1 = nums2[mid2-1] if mid2!=0 else float('-inf')
            y2 = nums2[mid2] if mid2!=n2 else float('inf')

            if x1 <= y2 and y1 <= x2:
                if (n1+n2)%2==0:
                    return (max(x1,y1)+min(x2,y2))/2
                else:
                    return max(x1,y1)
            elif x1 > y2:
                high = mid1-1
            else:
                low = mid1+1


class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums1 = [1]
        nums2 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 18
        self.assertEqual(expected, actual)
    def test_2(self):
        solution = Solution()
        nums1 = [1,2,3,4]
        nums2 = [5,6,7,8]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 4.5
        self.assertEqual(expected, actual)
    def test_3(self):
        solution = Solution()
        nums1 = [1,3,8,9,15]
        nums2 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 11
        self.assertEqual(expected, actual)
    def test_4(self):
        solution = Solution()
        nums1 = [0,0]
        nums2 = [0,0]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = 0.0
        self.assertEqual(expected, actual)

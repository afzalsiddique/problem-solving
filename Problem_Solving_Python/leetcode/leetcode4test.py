import unittest
from leetcode.leetcode4 import *

class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums1 = [1,3,8,9,15]
        nums2 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = float(11)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums2 = [1,3,8,9,15]
        nums1 = [7,11,18,19,21,25]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = float(11)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums2 = [1,3]
        nums1 = [2]
        actual = solution.findMedianSortedArrays(nums1, nums2)
        expected = float(2)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()
# https://www.youtube.com/watch?v=IzHR_U8Ly6c
import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,n
        while lo<hi:
            mid=(lo+hi)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[lo] and nums[mid] > nums[hi-1]:
                lo = mid+1
            elif nums[mid] <= nums[hi-1] and nums[mid] <= nums[lo]:
                hi = mid
            elif nums[mid] <= nums[hi-1] and nums[mid] >= nums[lo]:
                hi = mid
        return nums[lo]


class MyTestCase(unittest.TestCase):

    def test_11(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([0,1,2,3,4,5,6])
        self.assertEqual(expected, actual)

    def test_12(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([1,2,3,4,5,6,0])
        self.assertEqual(expected, actual)

    def test_13(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([2,3,4,5,6,0,1])
        self.assertEqual(expected, actual)

    def test_14(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([3,4,5,6,0,1,2])
        self.assertEqual(expected, actual)

    def test_15(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([4,5,6,0,1,2,3])
        self.assertEqual(expected, actual)

    def test_16(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([5,6,0,1,2,3,4])
        self.assertEqual(expected, actual)

    def test_17(self):
        sol = Solution()
        expected = 0
        actual = sol.findMin([6,0,1,2,3,4,5])
        self.assertEqual(expected, actual)

    # def test_18(self):
    #     sol = Solution()
    #     expected = 0
    #     actual = sol.findMin([0,0,0,0,4,5,6])
    #     self.assertEqual(expected, actual)
    #
    # def test_19(self):
    #     sol = Solution()
    #     expected = 0
    #     actual = sol.findMin([0,1,2,3,3,3,3])
    #     self.assertEqual(expected, actual)
    #
    # def test_20(self):
    #     sol = Solution()
    #     expected = 0
    #     actual = sol.findMin([5,6,0,1,1,1,1])
    #     self.assertEqual(expected, actual)
    #
    # def test_21(self):
    #     sol = Solution()
    #     expected = 0
    #     actual = sol.findMin([5,6,0,1,1,1,1])
    #     self.assertEqual(expected, actual)
    #
    # def test_22(self):
    #     sol = Solution()
    #     expected = 0
    #     actual = sol.findMin([4,4,4,4,5,6,0])
    #     self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 11
        actual = sol.findMin([11,13,15,17])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([3,4,5,1,2])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([1,2])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([2,1])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([1,5])
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([2,1,3])
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 1
        actual = sol.findMin([3,1,2])
        self.assertEqual(expected, actual)
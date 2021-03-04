# https://www.youtube.com/watch?v=sEQk8xgjx64
import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid  += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.firstBadVersion(0)
        expected = 0
        self.assertEqual(expected, actual)
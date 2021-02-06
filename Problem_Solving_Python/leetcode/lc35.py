from bisect import bisect_left
from typing import List
import unittest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(2, solution.searchInsert(nums = [1,3,5,6], target = 5))

    def test_2(self):
        solution = Solution()
        self.assertEqual(1, solution.searchInsert(nums = [1,3,5,6], target = 2))

    def test_3(self):
        solution = Solution()
        self.assertEqual(0, solution.searchInsert(nums = [1,3,5,6], target = 0))

    def test_4(self):
        solution = Solution()
        self.assertEqual(0, solution.searchInsert(nums = [1], target = 0))
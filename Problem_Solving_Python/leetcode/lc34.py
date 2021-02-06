# https://www.youtube.com/watch?v=edJ19qIL8WQ
import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=bisect_left(nums,target)
        if left==n or nums[left]!=target:
            return [-1,-1]
        right=bisect_right(nums,target)
        if right==0 or nums[right-1]!=target:
            return [left,-1]
        return [left,right-1]


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [3,4]
        actual = sol.searchRange(nums = [5,7,7,8,8,10], target = 8)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = [-1,-1]
        actual = sol.searchRange(nums = [5,7,7,8,8,10], target = 6)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = [-1,-1]
        actual = sol.searchRange(nums = [], target = 0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = [4,4]
        actual = sol.searchRange(nums = [5,7,7,7,8,10], target = 8)
        self.assertEqual(expected, actual)


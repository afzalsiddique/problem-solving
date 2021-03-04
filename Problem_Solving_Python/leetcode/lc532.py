import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        minn = nums[-1] - k
        cnt = 0
        for i in range(len(nums)):
            if nums[i] > minn:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            key = nums[i] + k
            idx = bisect_right(nums, key)
            idx -= 1
            if idx >= 0 and nums[idx] == key and idx!=i:
                cnt += 1
        return cnt

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.findPairs(nums = [3,1,4,1,5], k = 2)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.findPairs(nums = [1,2,3,4,5], k = 1)
        expected = 4
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.findPairs(nums = [1,3,1,5,4], k = 0)
        expected = 1
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.findPairs(nums = [1,2,4,4,3,3,0,9,2,3], k = 3)
        expected = 2
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.findPairs(nums = [-1,-2,-3], k = 1)
        expected = 2
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.findPairs(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.findPairs(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.findPairs(0)
        expected = 0
        self.assertEqual(expected, actual)
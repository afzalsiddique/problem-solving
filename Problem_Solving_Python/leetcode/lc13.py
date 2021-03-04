# https://www.youtube.com/watch?v=jzZsG8n2R9A
import unittest
from typing import List


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # nums sorted, impossible for nums[i]+nums[l]+nums[r] == 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue # prevent duplicates in result
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.threeSum(nums = [-1,0,1,2,-1,-4])
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.threeSum(0)
        expected = 0
        self.assertEqual(expected, actual)
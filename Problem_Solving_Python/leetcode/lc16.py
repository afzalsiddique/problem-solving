import unittest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    ans = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s
        return ans



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.threeSumClosest(nums = [-1,2,1,-4], target = 1)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.threeSumClosest([0,1,2], 3)
        expected = 3
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.threeSumClosest(0)
        expected = 0
        self.assertEqual(expected, actual)
import unittest
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        maxx = 0
        for r in range(n):
            if r>0 and nums[r-1]!=1 and nums[r]==1:
                l=r
            if nums[r] == 1 and nums[l] == 1:
                maxx = max(maxx, r - l + 1)
        return maxx

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.findMaxConsecutiveOnes([0,0,0,1,1,0,0,1,1,1])
        expected = 3
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.findMaxConsecutiveOnes([1,1,1,1,1])
        expected = 5
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.findMaxConsecutiveOnes([0,0])
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.findMaxConsecutiveOnes([0,1,0])
        expected = 1
        self.assertEqual(expected, actual)


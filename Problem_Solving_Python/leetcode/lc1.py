import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, num in enumerate(nums):
            if num in di:
                return [di[num],i]
            di[target-num] = i

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.twoSum(nums = [2,7,11,15], target = 9)
        expected = [0,1]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.twoSum(nums = [3,2,4], target = 6)
        expected = [1,2]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.twoSum(nums = [3,3], target = 6)
        expected = [0,1]
        self.assertEqual(expected, actual)


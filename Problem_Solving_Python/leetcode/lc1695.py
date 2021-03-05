import unittest
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        di = {}
        summ, maxx = 0, float('-inf')
        i = 0
        while i!=n:
            if nums[i] not in di:
                di[nums[i]] = i
                summ += nums[i]
                maxx = max(maxx, summ)
                i+=1
            else:
                temp = di[nums[i]] + 1
                di.pop(nums[i])
                i = temp
                summ = 0
                di = {}
        return maxx




class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [4,2,4,5,6]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 17
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [5,2,1,2,5,2,1,2,5]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 8
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [5,2,1,3]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 11
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [1,1,1,1,1,1]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [1,1,1,2,2,2,2]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 3
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [1,2,1,2,1,2,1,2]
        actual = solution.maximumUniqueSubarray(nums)
        expected = 3
        self.assertEqual(expected, actual)
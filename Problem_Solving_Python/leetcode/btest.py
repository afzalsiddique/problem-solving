import unittest
from leetcode.b import *

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
import unittest
from leetcode.leetcode53 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        actual = solution.maxSubArray(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [-2, -1]
        actual = solution.maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [-1]
        actual = solution.maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [1]
        actual = solution.maxSubArray(nums)
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [0]
        actual = solution.maxSubArray(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [-2, -3, -1]
        actual = solution.maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

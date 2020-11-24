import unittest
from leetcode.leetcode312 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3,1,5,8]
        actual = solution.maxCoins(nums)
        expected = 167
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [1,5,8]
        actual = solution.maxCoins(nums)
        expected = 56
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = []
        actual = solution.maxCoins(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [7,9,8,0,7,1,3,5,5,2,3]
        actual = solution.maxCoins(nums)
        expected = 1654
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [5,8]
        actual = solution.maxCoins(nums)
        expected =  48
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()

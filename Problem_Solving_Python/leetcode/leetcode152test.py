import unittest
from leetcode.leetcode152 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [2,3,-2,4]
        actual = solution.maxProduct(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_11(self):
        solution = Solution()
        nums = [2,3,-2,4, 0, 2,3,-2,4,-5]
        actual = solution.maxProduct(nums)
        expected = 240
        self.assertEqual(expected, actual)


    def test_2(self):
        solution = Solution()
        nums = [-2,0,-1]
        actual = solution.maxProduct(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [-2]
        actual = solution.maxProduct(nums)
        expected = -2
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

import unittest
from leetcode.lc416bimask2 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [5,4,2,2,4,3]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [1, 5, 11, 5]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [1, 2, 3, 5]
        actual = solution.canPartition(nums)
        expected = False
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [1, 1]
        actual = solution.canPartition(nums)
        expected = True
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

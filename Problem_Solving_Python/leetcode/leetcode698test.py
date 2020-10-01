import unittest
from leetcode.leetcode698 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [5,4,2,2,4,3]
        k = 2
        actual= solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [4,4,4,4]
        k = 4
        actual= solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [6,3,1,3,3,2,1,11,3,2,1,2,6,4]
        k = 4
        actual = solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        actual = solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [4,4,4,4]
        k = 2
        actual= solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [1,5,11,5]
        k = 2
        actual= solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [1,2,3,4]
        k = 3
        actual= solution.canPartitionKSubsets(nums, k)
        expected = False
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        nums = [10,10,10,7,7,7,7,7,7,6,6,6]
        k = 3
        actual= solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

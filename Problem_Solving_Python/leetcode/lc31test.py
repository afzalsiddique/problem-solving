from leetcode.lc31 import *
import unittest
class MyTestCase(unittest.TestCase):


    def test_2(self):
        solution = Solution()
        nums = [1,2,3]
        solution.nextPermutation(nums)
        expected = [1,3,2]
        self.assertEqual(expected, nums)

    def test_3(self):
        solution = Solution()
        nums = [3,2,1]
        solution.nextPermutation(nums)
        expected = [1,2,3]
        self.assertEqual(expected, nums)

    def test_4(self):
        solution = Solution()
        nums = [1,1,5]
        solution.nextPermutation(nums)
        expected = [1,5,1]
        self.assertEqual(expected, nums)

    def test_5(self):
        solution = Solution()
        nums = [1]
        solution.nextPermutation(nums)
        expected = [1]
        self.assertEqual(expected, nums)

    def test_6(self):
        solution = Solution()
        nums = [1,3,2]
        solution.nextPermutation(nums)
        expected = [2,1,3]
        self.assertEqual(expected, nums)

    def test_7(self):
        solution = Solution()
        nums = [1,5,1]
        solution.nextPermutation(nums)
        expected = [5,1,1]
        self.assertEqual(expected, nums)

    def test_8(self):
        solution = Solution()
        nums = [6,2,1,5,4,3,0]
        solution.nextPermutation(nums)
        expected = [6,2,3,0,1,4,5]
        self.assertEqual(expected, nums)

    def test_9(self):
        solution = Solution()
        nums = [6,2,1,5,4,3,3,0]
        solution.nextPermutation(nums)
        expected = [6,2,3,0,1,3,4,5]
        self.assertEqual(expected, nums)

    def test_10(self):
        solution = Solution()
        nums = [6,2,1,5,5,4,3,0]
        solution.nextPermutation(nums)
        expected = []
        self.assertEqual(expected, nums)
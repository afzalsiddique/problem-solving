import unittest
from leetcode.leetcode55dp import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [2,3,1,1,4]
        actual = solution.canJump(nums)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [3,1,0,0,4]
        actual = solution.canJump(nums)
        expected = False
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [0,2,3]
        actual = solution.canJump(nums)
        expected = False
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

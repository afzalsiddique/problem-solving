import unittest
from leetcode.lc493 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [1,3,2,3,1]
        expected = 2
        actual = sol.reversePairs(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        nums = [2,4,3,5,1]
        expected = 3
        actual = sol.reversePairs(nums)
        self.assertEqual(expected, actual)
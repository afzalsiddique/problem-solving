import unittest
from leetcode.lc315 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [7,8,11,12,13,4,5,6,9,10]
        expected = [3,3,5,5,5,0,0,0,0,0]
        actual = sol.countSmaller(nums)
        self.assertEqual(expected, actual)
    def test_2(self):
        sol = Solution()
        nums = [5,2,6,1]
        expected = [2,1,1,0]
        actual = sol.countSmaller(nums)
        self.assertEqual(expected, actual)
import unittest
from leetcode.lc209 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = 7
        nums = [2, 7, 2,2,2,1]
        actual = solution.minSubArrayLen(s, nums)
        self.assertEqual(1, actual)
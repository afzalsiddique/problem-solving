import unittest
from leetcode.lc122 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(7, solution.maxProfit([7,1,5,3,6,4]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.maxProfit([1,2,3,4,5]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(0, solution.maxProfit([7,6,4,3,1]))

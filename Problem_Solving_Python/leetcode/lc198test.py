import unittest
from leetcode.lc198 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(4, solution.rob([1, 2, 3, 1]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(12, solution.rob([2,7,9,3,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(0, solution.rob([]))
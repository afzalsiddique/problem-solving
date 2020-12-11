import unittest
from leetcode.lc213 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(3, solution.rob([2,3,2]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.rob([1,2,3,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(340, solution.rob([200,3,140,20,10]))
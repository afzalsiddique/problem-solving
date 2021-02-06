import unittest
from leetcode.lc279iterative import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(3, solution.numSquares(12))

    def test_2(self):
        solution = Solution()
        self.assertEqual(2, solution.numSquares(13))

    def test_3(self):
        solution = Solution()
        self.assertEqual(1, solution.numSquares(1))

    def test_4(self):
        solution = Solution()
        self.assertEqual(1, solution.numSquares(4))

    def test_5(self):
        solution = Solution()
        self.assertEqual(2, solution.numSquares(5))
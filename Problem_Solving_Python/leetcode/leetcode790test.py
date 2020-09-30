import unittest

from leetcode.leetcode790 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        N = 1
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 1
        self.assertEqual(expected,actual)

    def test_2(self):
        N = 2
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 2
        self.assertEqual(expected,actual)

    def test_3(self):
        N = 3
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 5
        self.assertEqual(expected,actual)

    def test_4(self):
        N = 4
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 11
        self.assertEqual(expected,actual)
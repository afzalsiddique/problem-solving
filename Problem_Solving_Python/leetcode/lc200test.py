import unittest
from leetcode.lc200 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        actual = solution.numIslands(grid)
        expected = 1
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        actual = solution.numIslands(grid)
        expected = 3
        self.assertEqual(expected, actual)
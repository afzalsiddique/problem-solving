import unittest
from leetcode.lc64 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        actual = solution.minPathSum(grid)
        expected = 7
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        grid = [[1,2,3],[4,5,6]]
        actual = solution.minPathSum(grid)
        expected = 12
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()

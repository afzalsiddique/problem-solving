import unittest
from leetcode.leetcode1277 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        matrix = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
        ]
        expected = 30
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        matrix = [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        expected = 7
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

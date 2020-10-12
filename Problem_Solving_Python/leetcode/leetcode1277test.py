import unittest
from leetcode.leetcode1277 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        matrix = [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
        ]
        expected = 14
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

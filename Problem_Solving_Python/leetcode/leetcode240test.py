import unittest
from leetcode.leetcode240 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        target = 10
        actual = solution.searchMatrix(matrix, target)
        expected = True
        self.assertEqual(expected, actual)


    def test_2(self):
        solution = Solution()
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        target = 20
        actual = solution.searchMatrix(matrix, target)
        expected = False
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        matrix = [
            [2]
        ]
        target = 20
        actual = solution.searchMatrix(matrix, target)
        expected = False
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        matrix = [
            [2]
        ]
        target = 2
        actual = solution.searchMatrix(matrix, target)
        expected = True
        self.assertEqual(expected, actual)


    def test_5(self):
        solution = Solution()
        matrix = [
            [2],
            [3],
            [4]
        ]
        target = 6
        actual = solution.searchMatrix(matrix, target)
        expected = False
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        matrix = [
            [2],
            [3],
            [4]
        ]
        target = 4
        actual = solution.searchMatrix(matrix, target)
        expected = True
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

import unittest
from leetcode.leetcode343 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        n = 2
        expected = 1
        actual = solution.integerBreak(n)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        n = 10
        expected = 36
        actual = solution.integerBreak(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

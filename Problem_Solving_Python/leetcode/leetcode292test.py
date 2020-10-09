import unittest
from leetcode.leetcode292 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        n = 1
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        n = 2
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        n = 3
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        n = 4
        expected = False
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        n = 5
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        n = 8
        expected = False
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

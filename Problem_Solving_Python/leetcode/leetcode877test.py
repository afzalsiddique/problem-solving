import unittest
from leetcode.leetcode877 import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        solution = Solution()
        piles = [5,3,4,5]
        actual = solution.stoneGame(piles)
        expected = True
        self.assertEqual(expected, actual)

    def test2(self):
        solution = Solution()
        piles = [5,3,4,5]
        actual = solution.stoneGame(piles)
        expected = True
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

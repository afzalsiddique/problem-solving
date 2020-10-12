import unittest
from leetcode.leetcode486 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        expected = False
        acutal = solution.PredictTheWinner([1, 5, 2])
        self.assertEqual(expected, acutal)

    def test_2(self):
        solution = Solution()
        expected = True
        acutal = solution.PredictTheWinner([1, 5, 233, 7])
        self.assertEqual(expected, acutal)

    def test_3(self):
        solution = Solution()
        expected = False
        acutal = solution.PredictTheWinner([1, 5, 3, 8, 2])
        self.assertEqual(expected, acutal)

    def test_4(self):
        solution = Solution()
        expected = True
        acutal = solution.PredictTheWinner([0])
        self.assertEqual(expected, acutal)


if __name__ == '__main__':
    unittest.main()

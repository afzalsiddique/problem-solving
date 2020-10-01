import unittest
from leetcode.leetcode322 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        coins = [1,2,5]
        amount = 11
        expected = 3
        actual = solution.coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        coins = [2]
        amount = 3
        expected = -1
        actual = solution.coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        coins = [1]
        amount = 0
        expected = 0
        actual = solution.coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        coins = [1]
        amount = 1
        expected = 1
        actual = solution.coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        coins = [1]
        amount = 2
        expected = 2
        actual = solution.coinChange(coins, amount)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

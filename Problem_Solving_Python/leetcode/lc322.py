import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        for row in dp:
            row[0] = 0
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount] != float('inf') else -1



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
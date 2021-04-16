import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        coins = [0] + coins
        dp=[[None]*(amount+1) for _ in range(n+1)]
        for j in range(amount+1):
            dp[0][j]=float('inf')
        for i in range(n+1):
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
        return dp[-1][-1] if dp[-1][-1]!=float('inf') else -1



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
import unittest
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        coins = [0] + coins
        dp=[[None]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,amount+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[-1][-1]
class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        amount = 5
        coins = [1,2,5]
        actual = solution.change(amount, coins)
        expected = 4
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        amount = 3
        coins = [2]
        actual = solution.change(amount, coins)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        amount = 10
        coins = [10]
        actual = solution.change(amount, coins)
        expected = 1
        self.assertEqual(expected, actual)
    def test4(self):
        self.assertEqual(1,Solution().change(0,[]))
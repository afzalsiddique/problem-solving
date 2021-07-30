import unittest


class Solution:
    def numTilings(self, N: int) -> int:
        mod = 1000000007
        dp = [[0]*4 for _ in range(N+1)]
        dp[0][3] = 1
        for i in range(1, N+1):
            dp[i][0] += dp[i-1][3] % mod

            dp[i][1] += dp[i-1][0] % mod
            dp[i][1] += dp[i-1][2] % mod

            dp[i][2] += dp[i-1][0] % mod
            dp[i][2] += dp[i-1][1] % mod

            dp[i][3] += dp[i-1][0] % mod
            dp[i][3] += dp[i-1][1] % mod
            dp[i][3] += dp[i-1][2] % mod
            dp[i][3] += dp[i-1][3] % mod

        return dp[N][3] % mod
class MyTestCase(unittest.TestCase):
    def test_1(self):
        N = 1
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 1
        self.assertEqual(expected,actual)

    def test_2(self):
        N = 2
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 2
        self.assertEqual(expected,actual)

    def test_3(self):
        N = 3
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 5
        self.assertEqual(expected,actual)

    def test_4(self):
        N = 4
        solution = Solution()
        actual = solution.numTilings(N)
        expected = 11
        self.assertEqual(expected,actual)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left][right-1], dp[left+1][right])
        return dp[0][n-1]

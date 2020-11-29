# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i + 1] = True
                ans = s[i:i+2]
        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n):
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
                    if right-left+1 > len(ans):
                        ans = s[left:right+1]
        return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        for left in range(n-1, -1, -1):
            for right in range(left+2,n):
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
        ans = 0
        for li in dp:
            ans += sum(li)
        return ans

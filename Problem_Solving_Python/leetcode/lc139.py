# https://www.youtube.com/watch?v=WepWFGxiwRs
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        di = {}
        for word in wordDict:
            di[word] = 1
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                word = s[i:j+1]
                if word in di:
                    dp[i][j] = True
                    continue
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] and dp[k+1][j])
        return dp[0][-1]
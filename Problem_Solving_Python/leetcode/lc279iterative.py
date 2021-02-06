# https://www.youtube.com/watch?v=1xfx6M_GqFk

# correct
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [x for x in range(n + 1)]
#         dp[0] = float('inf')
#         for num in range(4, n + 1):
#             minn = float('inf')
#             i = 1
#             while i * i <= num:
#                 if i * i == num:
#                     minn = 1
#                 else:
#                     minn = min(minn, dp[num - i * i] + 1)
#                 i += 1
#             dp[num] = minn
#         return dp[-1]


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        for num in range(1, n + 1):
            i = 1
            while i * i <= num:
                sq = i*i
                dp[num] = min(dp[num], 1+dp[num-sq])
                i += 1
        return dp[-1]

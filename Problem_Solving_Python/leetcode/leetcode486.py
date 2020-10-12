from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            memo[i][i] = nums[i]
        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                memo[l][r] = max(memo[l][l]-memo[l+1][r], memo[r][r]-memo[l][r-1])
        return True if memo[0][n-1] >= 0 else False














# from typing import List
#
#
# class Solution:
#     nums = []
#     memo = []
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         self.nums = nums
#         n = len(nums)
#         self.memo = [[float('inf')]*n for _ in range(n)]
#     def helper(self, l, r, player1, score):
#         if l>r:
#             return 0
#         if self.memo[l][r] != float('inf'):
#             return self.memo[l][r]
#         next = abs(player1-1)
#         if player1:
#             self.memo[l][r] = max(self.helper(l+1,r, next), self.helper(l, r+1, next))
#
#
#

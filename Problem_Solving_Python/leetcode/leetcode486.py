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





class Solution2:
    memo = []

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        self.memo = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.memo[i][i] = nums[i]
        return True if self.helper(0, n - 1) >= 0 else False

    def helper(self, left, right):
        if left == right:
            return self.memo[left][left]
        if self.memo[left][right] != float('inf'):
            return self.memo[left][right]
        option1 = self.memo[left][left] - self.helper(left + 1, right)
        option2 = self.memo[right][right] - self.helper(left, right - 1)
        self.memo[left][right] = max(option1, option2)
        return self.memo[left][right]

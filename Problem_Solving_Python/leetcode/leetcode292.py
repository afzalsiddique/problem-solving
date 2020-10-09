class Solution:
    dp = []

    def canWinNim(self, n: int) -> bool:
        self.dp = [[-1] * (n + 1) for _ in range(2)]
        return self.helper(n, 1)

    # ID == 0 is opponent
    # ID ==1 is me
    def helper(self, n, ID):
        if n == 0:
            if ID == 1:
                return False
            return True
        if 1 <= n <= 3:
            if ID == 1:
                return True
            return False
        if self.dp[ID][n] != -1:
            return self.dp[ID][n]

        next = abs(ID - 1)
        if ID == 1: # if it is my turn
            self.dp[ID][n] = max(self.helper(n - 1, next), self.helper(n - 2, next), self.helper(n - 3, next))
        else: # if it is opponent's turn
            self.dp[ID][n] = min(self.helper(n - 1, next), self.helper(n - 2, next), self.helper(n - 3, next))
        return self.dp[ID][n]

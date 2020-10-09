class Solution:
    memo = []

    def canWinNim(self, n: int) -> bool:
        self.memo = [[-1] * (n + 1) for _ in range(2)]
        return self.helper(n, 1)

    def helper(self, n, ID):
        if n == 0:
            if ID == 1:
                return False
            return True
        if 1 <= n <= 3:
            if ID == 1:
                return True
            return False
        if self.memo[ID][n] != -1:
            return self.memo[ID][n]

        next = abs(ID - 1)
        if ID == 1:
            self.memo[ID][n] = max(self.helper(n-1, next), self.helper(n-2, next), self.helper(n-3, next))
        else:
            self.memo[ID][n] = min(self.helper(n-1, next), self.helper(n-2, next), self.helper(n-3, next))
        return self.memo[ID][n]

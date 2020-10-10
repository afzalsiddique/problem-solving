# https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/864332/Minimax-with-DP-in-Python-(with-recursion-tree-plotted)
# https://www.youtube.com/watch?v=qBgxeaxX3l8

class Solution:

    def minAmt(self, l, h, dp):

        if (l, h) in dp:
            return dp[(l, h)]

        elif l >= h:
            return 0

        _min = float("+inf")
        for i in range(l, h + 1):
            _min = min(_min, i + max(self.minAmt(l, i - 1, dp), self.minAmt(i + 1, h, dp)))
        dp[(l, h)] = _min
        return _min

    def getMoneyAmount(self, n: int) -> int:
        return self.minAmt(1, n, dict())

solution = Solution()
solution.getMoneyAmount(5)
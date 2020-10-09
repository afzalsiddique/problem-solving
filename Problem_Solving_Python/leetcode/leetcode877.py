# https://leetcode.com/problems/stone-game/discuss/154660/Java-This-is-minimax-%2B-dp-(fully-detailed-explanation-%2B-generalization-%2B-easy-understand-code)

from typing import List


class Solution:
    memo = []

    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        self.memo = [[[-1] * (length + 1) for _ in range(length + 1)] for i in range(2)]
        return (self.helper(0, length-1, piles, 1)) >= 0

    def helper(self, l, r, piles, ID):
        if l > r:
            return 0
        if self.memo[ID][l][r] != -1:
            return self.memo[ID][l][r]

        next = abs(ID - 1)
        if ID == 1:
            self.memo[ID][l][r] = max(piles[l] + self.helper(l + 1, r, piles, next),
                                      piles[r] + self.helper(l, r - 1, piles, next))
        else:
            self.memo[ID][l][r] = min(-piles[l] + self.helper(l + 1, r, piles, next),
                                      -piles[r] + self.helper(l, r - 1, piles, next))
        return self.memo[ID][l][r]


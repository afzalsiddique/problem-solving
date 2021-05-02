import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    # iterative 1
    # https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        dp=[[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m][n-1]=1
        dp[m-1][n]=1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                needed = min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                if needed<1: # if we have extra hp that we don't need, then we need only 1 hp
                    needed=1
                dp[i][j]=needed
        return dp[0][0]
    # iterative 2
    # https://leetcode.com/problems/dungeon-game/discuss/745340/post-Dedicated-to-beginners-of-DP-or-have-no-clue-how-to-start

    # recursive 1
    # https://leetcode.com/problems/dungeon-game/discuss/745340/post-Dedicated-to-beginners-of-DP-or-have-no-clue-how-to-start


class tester(unittest.TestCase):
    def test1(self):
        dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
        Output= 7
        self.assertEqual(Output,Solution().calculateMinimumHP(dungeon))
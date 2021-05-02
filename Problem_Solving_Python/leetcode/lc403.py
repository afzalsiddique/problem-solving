import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        all_pos = set(stones)
        dp = {}
        def helper(pos,last_jump):
            if last_jump <= 0: return False
            if pos not in all_pos: return False
            if pos == stones[-1]: return True
            if (pos,last_jump) in dp: return dp[(pos,last_jump)]
            dp[(pos,last_jump)] = helper(pos+last_jump-1,last_jump-1) or helper(pos+last_jump,last_jump) or helper(pos+last_jump+1,last_jump+1)
            return dp[(pos,last_jump)]

        if stones[1]!=1: return False
        return helper(1,1)
# LIS
class Solution2:
    def canCross(self, stones):
        n = len(stones)
        if n == 0 or (n > 1 and stones[1] != 1):
            return False

        dp = [False for _ in range(n)]  # dp[i] means whether stone i can be reached or not
        dp[0] = dp[1] = True
        next_jump = defaultdict(set)   # to record the possible next jumps from stone i
        next_jump[1] = {0, 1, 2}

        for i in range(2, n):
            for j in range(1, i):
                need_jump = stones[i] - stones[j]
                if dp[j] and need_jump in next_jump[j]:
                    dp[i] = True
                    next_jump[i].update({need_jump-1,need_jump,need_jump+1})
        return dp[-1]

class tester(unittest.TestCase):
    def test1(self):
        stones = [0,1,3,5,6,8,12,17]
        Output= True
        self.assertEqual(Output,Solution().canCross(stones))
    def test2(self):
        stones = [0,1,2,3,4,8,9,11]
        Output= False
        self.assertEqual(Output,Solution().canCross(stones))

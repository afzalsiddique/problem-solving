from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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
    def test01(self):
        self.assertEqual(11,get_sol().calculateMinimumHP([[-10,1],[30,-5]]))
    def test02(self):
        self.assertEqual(1,get_sol().calculateMinimumHP([[0,5],[6,0]]))
    def test03(self):
        self.assertEqual(6,get_sol().calculateMinimumHP([[0,-5],[-6,0]]))
    def test04(self):
        self.assertEqual(7,get_sol().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))

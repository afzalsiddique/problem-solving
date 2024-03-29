from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution4:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dp(left): # think it from alice's perspective and assume to be maximizing agent
            if not left:
                return False
            i=1
            while left-i*i>=0:
                newLeft= left - i * i
                if not dp(newLeft):
                    return True
                i+=1
            return False

        return dp(n)
class Solution:
    # Think about this problem from alice perspective.
    # If we can find an idx where Alice loses and idx<i, then we can flip the result
    def winnerSquareGame(self, n: int) -> bool:
        dp=[None]*(n+1)
        dp[0]=False
        for stone in range(1,n+1):
            i=1
            ans=False
            while stone-i*i>=0:
                remainingStones=stone-i*i
                if dp[remainingStones]==False:
                    ans=True
                    break
                i+=1
            dp[stone]=ans
        return dp[-1]
class Solution3:
    def winnerSquareGame(self, n: int) -> bool:
        MAXIMIZER,MINIMIZER=True,False
        @cache
        def dfs(stone,player):
            if not stone:
                return not player
            if player==MAXIMIZER:
                i=1
                res=MINIMIZER
                while i*i<=stone:
                    if dfs(stone-i*i,not player):
                        return MAXIMIZER
                    i+=1
            else:
                i=1
                res=MAXIMIZER
                while i*i<=stone:
                    if not dfs(stone-i*i, not player):
                        return MINIMIZER
                    i+=1
            return res

        return dfs(n,MAXIMIZER)
class Solution2:
    # tle. minimax
    def winnerSquareGame(self, n: int) -> bool:
        def get_squares(n):
            return [i*i for i in range(1,int(sqrt(n))+1)]

        @cache
        def minimax(n,player):
            if n==0: return not player
            res=not player
            if player:
                for i in get_squares(n):
                    res=max(res,minimax(n-i,not player))
            else:
                for i in get_squares(n):
                    res=min(res,minimax(n-i,not player))
            return res

        return minimax(n,True)



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().winnerSquareGame(1))
    def test02(self):
        self.assertEqual(False, get_sol().winnerSquareGame(2))
    def test03(self):
        self.assertEqual(True, get_sol().winnerSquareGame(3))
    def test04(self):
        self.assertEqual(True, get_sol().winnerSquareGame(4))
    def test05(self):
        self.assertEqual(False, get_sol().winnerSquareGame(5))
    def test06(self):
        self.assertEqual(True, get_sol().winnerSquareGame(6))
    def test07(self):
        self.assertEqual(False, get_sol().winnerSquareGame(7))
    def test08(self):
        self.assertEqual(True, get_sol().winnerSquareGame(8))
    def test09(self):
        self.assertEqual(True, get_sol().winnerSquareGame(9))
    def test10(self):
        self.assertEqual(False, get_sol().winnerSquareGame(10))
    def test11(self):
        self.assertEqual(True, get_sol().winnerSquareGame(92719))


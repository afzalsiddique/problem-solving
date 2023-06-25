from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # time O(n) space O(n)
    # to achieve space O(1) follow the comments
    def stoneGameIII(self, nums: List[int]) -> str:
        n=len(nums)
        dp=[float('-inf')]*(n+1)
        dp[n]=0 # change 'n' to 'i%4'
        for i in range(n-1,-1,-1):
            take=0
            # dp[i%4]=float('-inf') # add this line
            for k in range(3):
                if i+k<n:
                    take+=nums[i+k]
                    dp[i]=max(dp[i],take-dp[i+k+1]) # change 'i' to 'i%4' and 'i+k+1' to '(i+k+1)%4'
        res=dp[0]
        return 'Alice' if res>0 else 'Bob' if res<0 else 'Tie'
class Solution2:
    # time O(n) space O(1)
    def stoneGameIII(self, nums: List[int]) -> str:
        n=len(nums)
        dp=[float('-inf')]*(3+1)
        dp[n%4]=0
        for i in range(n-1,-1,-1):
            take=0
            dp[i%4]=float('-inf')
            for k in range(3):
                if i+k<n:
                    take+=nums[i+k]
                    dp[i%4]=max(dp[i%4],take-dp[(i+k+1)%4])

        res=dp[0]
        return 'Alice' if res>0 else 'Bob' if res<0 else 'Tie'
class Solution5:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i): # think it from alice's perspective and assume to be maximizing agent
            if i>=n: return 0

            res=float('-inf')
            take=0
            for j in range(i,min(n,i+3)):
                take+=stoneValue[j]
                # take-dp(j+1) means myScore-Opponent's score
                res=max(res,take-dp(j+1))
            return res

        n=len(stoneValue)
        score = dp(0)
        return "Alice" if score>0 else "Bob" if score<0 else "Tie"
class Solution3:
    # bad solution
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def func(i:int,turn:int): # turn=1 -> alice's turn. turn=-1 -> bob's turn.
            if i>=n: return 0
            score=0
            best_max=float('-inf')
            best_min=float('inf')
            for j in range(3):
                if i+j<n:
                    score+=stoneValue[i+j]*turn
                    if turn==1:
                        best_max=max(score+func(i+j+1,turn*(-1)),best_max)
                    else:
                        best_min=min(score+func(i+j+1,turn*(-1)),best_min)
            if turn==1:
                return best_max
            return best_min


        n=len(stoneValue)
        res=func(0,1)
        return 'Alice' if res>0 else 'Bob' if res<0 else 'Tie'
class Solution4:
    # bad solution
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def func(i:int,turn:int): # turn=1 -> alice's turn. turn=-1 -> bob's turn.
            if i>=n: return 0
            score=0
            if turn==1:
                best=float('-inf')
                for j in range(3):
                    if i+j<n:
                        score+=stoneValue[i+j]*turn
                        best=max(score+func(i+j+1,turn*(-1)),best)
            else:
                best=float('inf')
                for j in range(3):
                    if i+j<n:
                        score+=stoneValue[i+j]*turn
                        best=min(score+func(i+j+1,turn*(-1)),best)
            return best


        n=len(stoneValue)
        res=func(0,1)
        return 'Alice' if res>0 else 'Bob' if res<0 else 'Tie'


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("Bob",get_sol().stoneGameIII([1,2,3,7]))
    def test2(self):
        self.assertEqual("Alice",get_sol().stoneGameIII([1,2,3,-9]))
    def test3(self):
        self.assertEqual("Tie",get_sol().stoneGameIII([1,2,3,6]))
    def test4(self):
        self.assertEqual("Tie",get_sol().stoneGameIII([-1,-2,-3]))
    def test5(self):
        self.assertEqual("Alice",get_sol().stoneGameIII([-1,-2]))
    def test6(self):
        self.assertEqual("Tie",get_sol().stoneGameIII([-1,-3,-2]))
    # def test7(self):
    # def test8(self):
    # def test9(self):

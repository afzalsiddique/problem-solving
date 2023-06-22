from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution2()
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i,j):
            if i==j:
                return piles[i]

            take1=piles[i]
            # take-dp(..) -> myScore-Opponent's score.
            option1=take1-dp(i+1,j)

            take2=piles[j]
            # take-dp(..) -> myScore-Opponent's score.
            option2=take2-dp(i,j-1)

            return max(option1,option2)

        res=dp(0,len(piles)-1)
        return True if res>0 else False
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        to_win=sum(piles)//2+1
        dp = {}
        def helper(left, right, turn, alex, lee):
            if left>right:
                if alex>=to_win: return True
                return False
            if (left,right,turn) in dp: return dp[(left,right,turn)]
            ans = False
            if turn: # if alex's turn
                # pick left
                if helper(left+1, right, not turn, alex + piles[left], lee):
                    ans = True
                # pick right
                if helper(left,right-1, not turn, alex + piles[right], lee):
                    ans = True
            else: # not alex's turn
                if helper(left+1, right, not turn, alex, lee + piles[left]):
                    ans = True
                if helper(left,right-1, not turn, alex, lee + piles[right]):
                    ans = True
            dp[(left,right,turn)] = ans
            return ans

        return helper(0,len(piles)-1,True,0,0)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().stoneGame([5,3,4,5]))
    def test02(self):
        self.assertEqual(True, get_sol().stoneGame([5,3,4,5]))

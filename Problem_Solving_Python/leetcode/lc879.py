from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # space O(G*P*len(group))
    # time O(G*P*len(group))
    # https://leetcode.com/problems/profitable-schemes/discuss/157099/Java-original-3d-to-2d-DP-solution
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD=10**9+7
        # dp[c][g][p] means for first c crime with g members and at least p profit, what is total schemes can be chosen.
        dp=[[[0 for _ in range(P+1)] for __ in range(G+1)] for ___ in range(len(group)+1)]
        dp[0][0][0] = 1 # not commit for any crime, that's one scheme
        # INCLUDE EXCLUDE type scenario. KNAPSACK
        for c in range(1,len(group)+1):
            thisGroup=group[c-1]
            thisProfit=profit[c-1]
            for g in range(G+1):
                for p in range(P+1):
                    dp[c][g][p]=dp[c-1][g][p] # EXCLUDE the crime
                    # we need this condition because without g members we cannot commit this crime
                    if g>=thisGroup:

                        # the reason why it is [max(0,p-thisProfit)] is because we want schemes with 'AT LEAST' P profit.
                        # If p-thisProfit is less than 0, then this means only this crime itself is making P profit.
                        dp[c][g][p] +=dp[c-1][g-thisGroup][max(0,p-thisProfit)] # INCLUDE the crime
                        dp[c][g][p] %= MOD
        res=0
        for g in range(G+1):
            res = (res + dp[-1][g][P]) %MOD
        return res
class Solution2:
    # space O(G*P)
    # time O(G*P*len(group)
    # https://leetcode.com/problems/profitable-schemes/discuss/157099/Java-original-3d-to-2d-DP-solution
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD=10**9+7
        dp=[[0 for _ in range(P+1)] for __ in range(G+1)]
        dp[0][0]=1  # not commit for any crime, that's one scheme
        for c in range(1,len(group)+1):
            thisGroup=group[c-1]
            thisProfit=profit[c-1]
            for g in range(G,-1,-1): # It tries to get correct old k - 1 dimension value, if still traverse from left to right,
                # the new value will override the old k - 1 dimension value
                # which will be needed in the upcoming iterations
                for p in range(P,-1,-1):
                    if g>=thisGroup:
                        dp[g][p]+=dp[g-thisGroup][max(0,p-thisProfit)]
                        dp[g][p]%=MOD

        res=0
        for g in range(G+1):
            res+=dp[g][-1]
            res%=MOD
        return res
class Solution3:
    # tle
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(start:int,curProfit:int,memberLeft:int):
            ans=0
            if memberLeft<0:
                return 0
            if curProfit>=minProfit:
                ans+=1
            for i in range(start,len(group)):
                ans+=dfs(i+1,curProfit+profit[i],memberLeft-group[i])
                ans%=MOD
            return ans

        MOD=10**9+7
        return dfs(0,0,n)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().profitableSchemes( 5,  3,  [2,2], [2,3]))
    def test2(self):
        self.assertEqual(7, get_sol().profitableSchemes( 10,  5,  [2,3,5], [6,7,8]))
    def test3(self):
        self.assertEqual(188883405, get_sol().profitableSchemes(100, 10, [66,24,53,49,86,37,4,70,99,68,14,91,70,71,70,98,48,26,13,86,4,82,1,7,51,37,27,87,2,65,93,66,99,28,17,93,83,91,45,3,59,87,92,62,77,21,9,37,11,4,69,46,70,47,28,40,74,47,12,3,85,16,91,100,39,24,52,50,40,23,64,22,2,15,18,62,26,76,3,60,64,34,45,40,49,11,5,8,40,71,12,60,3,51,31,5,42,52,15,36], [8,4,8,8,9,3,1,6,7,10,1,10,4,9,7,11,5,1,7,4,11,1,5,9,9,5,1,10,0,10,4,1,1,1,6,9,3,6,2,5,4,7,8,5,2,3,0,6,4,5,9,9,10,7,1,8,9,6,0,2,9,2,2,8,6,10,3,4,6,1,10,7,5,4,8,1,8,5,5,4,1,1,10,0,8,0,1,11,5,4,7,9,1,11,1,0,1,6,8,3]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

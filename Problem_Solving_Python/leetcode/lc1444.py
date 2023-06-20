from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/discuss/623732/JavaC%2B%2BPython-DP-%2B-PrefixSum-in-Matrix-Clean-code
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(r, c, k):
            if pre[r][c]==0: # does not contain apple
                return 0
            if k==0:
                return 1

            res=0
            # cut horizontally
            for i in range(r+1, m):
                if pre[r][c]-pre[i][c]>=1: # contains apple
                    res+=dfs(i, c, k-1)
                    res%=MOD

            # cut vertically
            for j in range(c+1, n):
                if pre[r][c]-pre[r][j]>=1: # contains apple
                    res+=dfs(r,j, k-1)
                    res%=MOD

            return res

        m,n=len(pizza),len(pizza[0])
        pre=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                pre[i][j]=pre[i+1][j]+pre[i][j+1]-pre[i+1][j+1]+(1 if pizza[i][j]=='A' else 0)

        return dfs(0,0,k-1)

class Solution2:
    def createDP(self,pizza:List[str]):
        m,n=len(pizza),len(pizza[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+(pizza[i-1][j-1]=='A')
        return dp
    def ways(self, pizza: List[str], k: int) -> int:
        M=10**9+7
        @cache
        def dfs(r1,r2,c1,c2,k):
            if k==0:
                return int(hasApples(r1,r2,c1,c2))
            res=0
            for j in range(c1,c2):
                if hasApples(r1,r2,c1,j):
                    res+= dfs(r1,r2,j+1,c2,k-1)
            for i in range(r1,r2):
                if hasApples(r1,i,c1,c2):
                    res+= dfs(i+1,r2,c1,c2,k-1)
            return res%M
        def hasApples(r1,r2,c1,c2):
            return dp[r2+1][c2+1]-dp[r2+1][c1]-dp[r1][c2+1]+dp[r1][c1]>=1

        m,n=len(pizza),len(pizza[0])
        dp=self.createDP(pizza)
        return dfs(0,m-1,0,n-1,k-1)
class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().ways(["A..","AAA","..."],  3))
    def test2(self):
        self.assertEqual(1, get_sol().ways(["A..","AA.","..."],  3))
    def test3(self):
        self.assertEqual(1, get_sol().ways(["A..","A..","..."], 1))
    def test4(self):
        self.assertEqual(641829390, get_sol().ways(["..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA","A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.","A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA","....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.","AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..","....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA","A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.","A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..","A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....","..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.","...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A","A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...","A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA","AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A","...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA","..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A","AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A","A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...","..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..","A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..","A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA","A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....","A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.","A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...","AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..","A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....","A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA","..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..","AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA","..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A","AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA","AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.","......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.","AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",".AA.A...AA.AAA.A....A.A...A........A.AAA......A...","..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..","..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.","...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.","..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"], 8))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
    # def test10(self):

from itertools import accumulate,permutations,product; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList,SortedDict
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/painting-a-grid-with-three-different-colors/discuss/1330174/Top-down-DP-with-bit-mask/1015776
    # 0-> no color 1-> red 2->green 3-> blue
    # draw the grid like this: kind of inverted
    #     <---i----> 'm' th row
    #  ^  | 1 | 2 | 3 |
    #  |  | 3 | 1 | 2 |
    #  |
    #  j
    #  |
    #  'n' th column
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD=10**9+7
        def dfs(i, j, prev, cur):
            if i==m:
                return dfs(0, j + 1, cur, 0)
            if j ==n:
                return 1
            if i==0 and (j, prev) in dp:
                return dp[j, prev]
            result = 0
            left = 0 if i == 0 else cur & 3 # 3 in binary -> '11'. So it is taking least two significant bits
            up = prev >> (i * 2) & 3
            for color in range(1,3+1):
                if left!=color and up!= color:
                    # cur              -> '000010'
                    # cur<<2           -> '001000'
                    # color            -> '000011'
                    # (cur<<2) | color -> '001011'
                    newCur=(cur << 2) | color
                    result = (result + dfs(i + 1, j, prev, newCur)) % MOD
            if i==0:
                dp[j, prev] = result
            return result

        dp={}
        return dfs(0, 0, 0, 0)
class Solution2:
    def getAllPerm(self,m):
        def check(A): return all(x != y for x, y in zip(A, A[1:])) # no same color in two adjacent cell in the same col
        nums=[1, 2, 3]
        n1=min(m,3)
        perm1 = permutations(nums, n1)
        perm2 = permutations(nums, max(0,m-n1))
        res=[]
        for x,y in product(perm1,perm2):
            a = list(x)+list(y)
            if check(a):
                res.append(a)
        return res
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD=10**9+7
        def checkPrev(A,B): return all(x!=y for x,y in zip(A,B)) # no same color in two adjacent columns
        def dfs(n,prev):
            if n==0:
                return 1
            res=0
            for perm in perms:
                perm=tuple(perm)
                if checkPrev(perm,prev):
                    res+=dfs(n-1,perm)
                    res%=MOD
            return res

        perms=self.getAllPerm(m)
        start=[-i for i in range(1,m+1)]
        return dfs(n,tuple(start))

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().colorTheGrid(1,1))
    def test2(self):
        self.assertEqual(6, get_sol().colorTheGrid(1,2))
    def test3(self):
        self.assertEqual(580986, get_sol().colorTheGrid(5,5))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
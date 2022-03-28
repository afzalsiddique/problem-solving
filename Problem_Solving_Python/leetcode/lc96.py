from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=CMaZ69P1bAc

class Solution:
    # recursive dp
    def numTrees(self, n: int) -> int:
        dp = {}
        def catalan(n):
            if n==0 or n==1: return 1
            if n in dp: return dp[n]
            ans =0
            for i in range(n):
                ans+=catalan(i)*catalan(n-i-1)
            dp[n]=ans
            return dp[n]
        return catalan(n)
class Solution2:
    # iterative dp
    def numTrees(self, n: int) -> int:
        def catalan(nth):
            dp = [0]*(nth+1)
            dp[0] = dp[1] = 1
            if nth == 0 or nth == 1: return 1
            for n in range(2, nth + 1):
                for i in range(n):
                    dp[n] += dp[i] * dp[n-i-1]
            return dp[nth]

        return catalan(n)

class Solution3:
    # binomial coefficient
    def numTrees(self, n: int) -> int:
        di={}
        def factorial(n):
            if n==0 or n==1: return 1
            if n in di: return di[n]
            di[n]=n*factorial(n-1)
            return di[n]

        def catalan(n):
            return factorial(2*n) / factorial(n) / factorial(n+1)

        return int(catalan(n))

class Solution4:
    def numTrees(self, n: int) -> int:
        @cache
        def count(left,right):
            if left>right:
                return 0
            if left==right:
                return 1
            res=0
            for i in range(left,right+1):
                l=count(left,i-1)
                r=count(i+1,right)
                if l and r:
                    res+=l*r
                else:
                    res+=l+r
            return res

        return count(1,n)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().numTrees(1))
    def test02(self):
        self.assertEqual(2, get_sol().numTrees(2))
    def test03(self):
        self.assertEqual(5, get_sol().numTrees(3))
    def test04(self):
        self.assertEqual(14, get_sol().numTrees(4))
    def test05(self):
        self.assertEqual(1767263190, get_sol().numTrees(19))

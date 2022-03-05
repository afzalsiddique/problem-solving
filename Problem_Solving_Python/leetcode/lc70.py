from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # time O(n) mem O(1)
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        dp=[1,2] # when n==1 dp[]=1; when n==2: dp[]=2
        res=0
        for i in range(3,n+1):
            res=dp[0]+dp[1]
            dp[0]=dp[1]
            dp[1]=res
        return res
class Solution3:
    # time O(n) mem O(n)
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(n):
            if n==1: return 1
            if n==2: return 2
            return dp(n-1)+dp(n-2)
        return dp(n)



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().climbStairs(2))
    def test02(self):
        self.assertEqual(3,get_sol().climbStairs(3))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):

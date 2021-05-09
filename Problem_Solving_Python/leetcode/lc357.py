import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    # back tracking
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.count=0
        vis=[False]*10
        def helper(num):
            if num>=self.maxx:
                return
            self.count+=1
            for i in range(10):
                if i==0 and num==0: continue # skip leading zeros
                if vis[i]==False:
                    vis[i]=True
                    helper(num*10+i)
                    vis[i]=False

        if n>10: n=10 # Cannot exceeds 10 digits without duplicate digits
        self.maxx=pow(10,n)
        helper(0)
        return self.count

class Solution2:
    # dp
    # https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83052/Clear-c%2B%2B-explanation-of-combinatorics-using-DP-method
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            # if i==1: ans = dp[i-1] + (9)
            # if i==2: ans = dp[i-1] + (9) * 9
            # if i==3: ans = dp[i-1] + (9) * 9*8
            # if i==4: ans = dp[i-1] + (9) * 9*8*7
            temp=9
            ans=9
            for _ in range(2,i+1):
                ans*=temp
                temp-=1
            dp[i]=dp[i-1]+ans
        return dp[-1]

class tester(unittest.TestCase):
    def test01(self):
        n=0
        Output= 1
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
    def test02(self):
        n=1
        Output= 10
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
    def test03(self):
        n=2
        Output= 91
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
    def test04(self):
        n=3
        Output= 739
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
    def test05(self):
        n=4
        Output= 5275
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))

import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()
class Solution:
    def minSteps(self, n: int) -> int:
        steps=0
        cur=1
        last_copied=0
        while cur!=n:
            if (n-cur)%cur==0:
                steps+=1 # copy
                steps+=1 # paste
                last_copied=cur
                cur*=2
            else:
                steps+=1 # paste
                cur+=last_copied
        return steps
class Solution2:
    # dp
    # longest increasing subsequence
    def minSteps(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        if n==1: return 0
        if n==2: return 2
        dp[1]=0
        dp[2]=2
        for i in range(3,n+1):
            for j in range(1,i):
                if i%j==0:
                    dp[i]=min(dp[i],dp[j]+i//j)
        return dp[-1]
class mytestcase(unittest.TestCase):
    def test01(self):
        n=1
        Output=0
        self.assertEqual(Output,get_sol().minSteps(n))
    def test02(self):
        n=2
        Output=2
        self.assertEqual(Output,get_sol().minSteps(n))
    def test03(self):
        n=3
        Output=3
        self.assertEqual(Output,get_sol().minSteps(n))
    def test04(self):
        n=4
        Output=4
        self.assertEqual(Output,get_sol().minSteps(n))
    def test05(self):
        n=5
        Output=5
        self.assertEqual(Output,get_sol().minSteps(n))
    def test06(self):
        n=6
        Output=5
        self.assertEqual(Output,get_sol().minSteps(n))

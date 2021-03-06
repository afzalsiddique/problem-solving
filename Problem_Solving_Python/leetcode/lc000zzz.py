import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=hqGa65Rp5LQ
    # https://www.youtube.com/watch?v=MqYLmIzl8sQ
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        summ=sum(stones)
        stones = ['#'] + stones
        dp = [[0]*(summ+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for j in range(1, summ + 1):
            dp[0][j] = False
        for i in range(1,n+1):
            for j in range(1,summ+1):
                # exclude
                dp[i][j]=dp[i-1][j]
                if j>=stones[i]:
                    dp[i][j]|=dp[i-1][j-stones[i]]

        diff = float('inf')
        for sum1 in range(summ//2,-1,-1):
            if dp[-1][sum1]:
                sum2=summ-sum1
                diff=abs(sum2-sum1)
                break
        for x in dp: print(x)
        return diff
class Solution2:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        S=sum(stones)
        S2=0
        dp=[[0]*(n+1) for _ in range(S+1)]
        for j in range(n+1):
            dp[0][j]=1
        for i in range(1,n+1):
            for s in range(1,S//2+1):
                if dp[s][i-1] or (s>=stones[i-1] and dp[s-stones[i-1]][i-1]):
                    dp[s][i]=1
                    S2=max(S2,s)
        for x in dp: print(x)
        return S-2*S2



class tester(unittest.TestCase):
    def test_1(self):
        stones = [2,7,4,1,8,1]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_2(self):
        stones = [31,26,33,21,40]
        Output= 5
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_3(self):
        stones = [1,2]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_4(self):
        stones = [2,6,4,1]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    # def test_5(self):
    # def test_6(self):

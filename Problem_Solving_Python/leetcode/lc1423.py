import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        cum_sum_left=[0]*(k+1)
        cum_sum_right=[0]*(k+1)

        tmp=0
        j=1
        for i in range(min(n,k)):
            tmp+=cardPoints[i]
            cum_sum_left[j]=tmp
            j+=1

        tmp=0
        j=k-1
        for i in range(n-1,n-k-1,-1):
            tmp+=cardPoints[i]
            cum_sum_right[j]=tmp
            j-=1

        # print(cum_sum_left)
        # print(cum_sum_right)
        maxx=float('-inf')
        for i in range(k+1):
            maxx=max(maxx,cum_sum_left[i]+cum_sum_right[i])
        return maxx
class tester(unittest.TestCase):
    def test1(self):
        cardPoints = [1,2,3,4,5,6,1]
        k = 3
        Output= 12
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
    def test2(self):
        cardPoints = [2,2,2]
        k = 2
        Output= 4
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
    def test3(self):
        cardPoints = [9,7,7,9,7,7,9]
        k = 7
        Output= 55
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
    def test4(self):
        cardPoints = [1,1000,1]
        k = 1
        Output= 1
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
    def test5(self):
        cardPoints = [1,79,80,1,1,1,200,1]
        k = 3
        Output= 202
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
    def test6(self):
        cardPoints = [96,90,41,82,39,74,64,50,30]
        k = 8
        Output= 536
        self.assertEqual(Output,get_sol().maxScore(cardPoints,k))
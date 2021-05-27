import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        cum_sum_left=[]
        cum_sum_right=[]
        tmp=0
        for i in range(min(n,k)):
            tmp+=cardPoints[i]
            cum_sum_left.append(tmp)
        tmp=0
        for i in reversed(range(min(n,k))):
            tmp+=cardPoints[i]
            cum_sum_right.append(tmp)
        maxx=float('inf')
        for i in range(k):
            maxx=max(maxx,cum_sum_left[i]+cum_sum_right[k-i-1])
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
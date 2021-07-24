import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n=len(profit)
        jobs=[[difficulty[i],profit[i]] for i in range(n)]
        jobs.sort(key=lambda x:(x[0],-x[1]))
        difficulty=[jobs[i][0] for i in range(n)]
        profit=[jobs[i][1] for i in range(n)]

        # for i in range(n): print(difficulty[i],profit[i])
        # print()

        maxx=profit[0]
        for i in range(1,n):
            maxx=max(maxx,profit[i]) # running max profit
            profit[i]=maxx

        # for i in range(n): print(difficulty[i],profit[i])

        res=0
        for w in worker:
            idx=bisect_right(difficulty,w)
            idx-=1
            if difficulty[idx]<=w: # if this worker can do the job
                res+=profit[idx] # add profit
        return res



class tester(unittest.TestCase):
    def test_1(self):
        difficulty,profit ,worker= [2,4,6,8,10],   [10,20,30,40,50],   [4,5,6,7]
        Output= 100
        self.assertEqual(Output, get_sol().maxProfitAssignment(difficulty,profit,worker))
    def test_2(self):
        difficulty,profit ,worker= [85,47,57],   [24,66,99],   [40,25,25]
        Output= 0
        self.assertEqual(Output, get_sol().maxProfitAssignment(difficulty,profit,worker))
    def test_3(self):
        difficulty,profit ,worker= [68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]
        Output= 324
        self.assertEqual(Output, get_sol().maxProfitAssignment(difficulty,profit,worker))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
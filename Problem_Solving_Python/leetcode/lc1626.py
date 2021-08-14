import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # lis
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n=len(scores)
        ages,scores=zip(*sorted(zip(ages,scores),key=lambda x:(-x[0],-x[1])))
        dp = [s for s in scores]
        for i in range(n):
            for j in range(i):
                if scores[j]>=scores[i]:
                    dp[i]=max(dp[i],dp[j]+scores[i])
        # print(ages)
        # print(scores)
        # print(dp)
        return max(dp)



class MyTestCase(unittest.TestCase):
    def test_1(self):
        scores,ages= [1,3,5,10,15],[1,2,3,4,5]
        Output= 34
        self.assertEqual(Output, get_sol().bestTeamScore(scores,ages))
    def test_2(self):
        scores,ages= [4,5,6,5],[2,1,2,1]
        Output= 16
        self.assertEqual(Output, get_sol().bestTeamScore(scores,ages))
    def test_3(self):
        scores,ages= [1,2,3,5],[8,9,10,1]
        Output= 6
        self.assertEqual(Output, get_sol().bestTeamScore(scores,ages))
    def test_4(self):
        scores,ages= [319776,611683,835240,602298,430007,574,142444,858606,734364,896074], [1,1,1,1,1,1,1,1,1,1]
        Output= 5431066
        self.assertEqual(Output, get_sol().bestTeamScore(scores,ages))
    def test_5(self):
        scores,ages= [1,3,7,3,2,4,10,7,5], [4,5,2,1,1,2,4,1,4]
        Output= 29
        self.assertEqual(Output, get_sol().bestTeamScore(scores,ages))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

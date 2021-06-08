import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        r=0
        for i in range(n):
            left_smaller,left_greater,right_smaller,right_greater=0,0,0,0
            for j in range(n):
                if i==j: continue
                if j < i:
                    if rating[j] < rating[i]:
                        left_smaller+=1
                    else:
                        left_greater+=1
                elif j > i:
                    if rating[j] < rating[i]:
                        right_smaller+=1
                    else:
                        right_greater+=1
            r+= left_smaller*right_greater+left_greater*right_smaller
        return r

class Solution2:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        up = [0] * n
        down = [0] * n
        teams = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                else:
                    down[i] += 1
                    teams += down[j]

        return teams
class tester(unittest.TestCase):
    def test1(self):
        rating = [2,5,3,4,1]
        Output= 3
        self.assertEqual(Output,get_sol().numTeams(rating))
    def test2(self):
        rating = [2,1,3]
        Output= 0
        self.assertEqual(Output,get_sol().numTeams(rating))
    def test3(self):
        rating = [1,2,3,4]
        Output= 4
        self.assertEqual(Output,get_sol().numTeams(rating))
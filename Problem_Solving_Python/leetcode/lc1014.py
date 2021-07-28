import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        prev_score=values[0]
        res=0
        for i in range(1,n):
            prev_score-=1
            res=max(res,prev_score+values[i])
            if values[i]>prev_score:
                prev_score=values[i]
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        values = [8,1,5,2,6]
        Output= 11
        self.assertEqual(Output,Solution().maxScoreSightseeingPair(values))
    def test_2(self):
        values = [1,2]
        Output= 2
        self.assertEqual(Output,Solution().maxScoreSightseeingPair(values))
    def test_3(self):
        values = [8,1,5,2,6,7]
        Output= 12
        self.assertEqual(Output,Solution().maxScoreSightseeingPair(values))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
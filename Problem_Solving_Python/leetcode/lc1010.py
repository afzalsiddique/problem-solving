import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=toYgBIaUdfM&t=163s
    # https://www.youtube.com/watch?v=wxqN1HX4Djk
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def nC2(n): return n*(n-1)//2 # no of ways to choose 2 items out of n items
        count = [0]*60
        for t in time:
            count[t%60]+=1
        total=0
        for i in range(1,30):
            total+= count[i]* count[60-i]
        total+=nC2(count[0])
        total+=nC2(count[30])
        return total

class tester(unittest.TestCase):
    def test1(self):
        time = [30,20,150,100,40]
        Output= 3
        self.assertEqual(Output,get_sol().numPairsDivisibleBy60(time))
    def test2(self):
        time = [60,60,60]
        Output= 3
        self.assertEqual(Output,get_sol().numPairsDivisibleBy60(time))

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        def dfs(i,maxDoubles):
            if i==1:
                return 0
            cnt=0
            while i>1 and maxDoubles:
                if i%2:
                    i-=1
                    cnt+=1
                i=i//2
                cnt+=1
                maxDoubles-=1
            option1=float('inf')
            if i==1:
                return cnt
            option2=cnt+(i-1)
            return min(option1,option2)

        return dfs(target,maxDoubles)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().minMoves(target = 5, maxDoubles = 0))
    def test2(self):
        self.assertEqual(7,get_sol().minMoves(target = 19, maxDoubles = 2))
    def test3(self):
        self.assertEqual(4,get_sol().minMoves(target = 10, maxDoubles = 4))
    def test4(self):
        self.assertEqual(4,get_sol().minMoves(target = 10, maxDoubles = 4))
    # def test5(self):

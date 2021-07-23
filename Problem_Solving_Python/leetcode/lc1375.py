import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        pq = []
        ans=0
        for k in range(len(light)):
            heappush(pq,-light[k])
            top=-pq[0]
            if top==k+1 and len(pq)==k+1:
                ans+=1
        return ans
class tester(unittest.TestCase):
    def test_1(self):
        light = [2,1,3,5,4]
        Output= 3
        self.assertEqual(Output,get_sol().numTimesAllBlue(light))
    def test_2(self):
        light = [3,2,4,1,5]
        Output= 2
        self.assertEqual(Output,get_sol().numTimesAllBlue(light))
    def test_3(self):
        light = [4,1,2,3]
        Output= 1
        self.assertEqual(Output,get_sol().numTimesAllBlue(light))
    def test_4(self):
        light = [2,1,4,3,6,5]
        Output= 3
        self.assertEqual(Output,get_sol().numTimesAllBlue(light))
    def test_5(self):
        light = [1,2,3,4,5,6]
        Output= 6
        self.assertEqual(Output,get_sol().numTimesAllBlue(light))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

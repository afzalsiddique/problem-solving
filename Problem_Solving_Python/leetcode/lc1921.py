import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pq = [d/s for d,s in zip(dist,speed)]
        heapify(pq)
        ans=0
        while pq:
            tmp=heappop(pq)
            if tmp<=ans:
                return ans
            ans+=1
        return ans

class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums = [1,2,2]
        Output= 1
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_02(self):
        nums = [3,2,1,2,1,7]
        Output= 6
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_03(self):
        nums = [0,0]
        Output= 1
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_04(self):
        nums = [4,4,4,5,5,5,15,15,15,16,16]
        Output= 20
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_05(self):
        nums = [3,2,1,2,1,7]
        Output= 6
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_06(self):
        nums = []
        Output= 0
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    # def test_07(self):
    # def test_08(self):

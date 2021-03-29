from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx,total,left=0,0,0
        for i in range(len(cost)):
            left = left + gas[i] - cost[i]
            total = total + gas[i] - cost[i]
            if left<0:
                left=0
                idx=i+1
        return idx if total>=0 else -1

class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(3, Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    def test_2(self):
        self.assertEqual(-1, Solution().canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
    def test_3(self):
        self.assertEqual(0, Solution().canCompleteCircuit(gas = [2,3,4], cost = [2,3,4]))

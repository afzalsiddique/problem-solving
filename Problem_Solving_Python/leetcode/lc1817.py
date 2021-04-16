from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        di = defaultdict(set)
        for id,time in logs:
            di[id].add(time)
        for id in di:
            di[id] = len(di[id])
        res = [0]*k
        for id in di:
            time = di[id]-1
            res[time] += 1
        return res

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,2,0,0,0],Solution().findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]],5))
    def test2(self):
        self.assertEqual([1,1,0,0],Solution().findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))


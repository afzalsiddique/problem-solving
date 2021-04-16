from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    # https://www.youtube.com/watch?v=tGw5GbDekTU
    def leastInterval(self, tasks, n):
        curr_time, di = 0, defaultdict(int)
        for t in tasks: di[t]+=1
        pq = []
        for v in di.values(): heappush(pq, -1*v)
        while pq:
            li = []
            for _ in range(n+1):
                curr_time += 1
                if pq:
                    x = heappop(pq) * (-1)
                    if x != 1: # not finished
                        li.append(x-1)
                if not pq and not li:
                    break
            for val in li:
                heappush(pq, -val)
        return curr_time

class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(8,Solution().leastInterval(["A","A","A","B","B","B"], 2))
    def test2(self):
        self.assertEqual(6,Solution().leastInterval(["A","A","A","B","B","B"], 0))
    def test3(self):
        self.assertEqual(16,Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

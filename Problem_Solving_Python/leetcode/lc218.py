import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List




class Solution:
    # https://leetcode.com/problems/the-skyline-problem/discuss/954585/Python-O(n-log-n)-solution-using-heap-explained
    # https://www.youtube.com/watch?v=GSBLe8cKu0s
    def getSkyline(self, buildings):
        # For each building, put two tuples of information to points: for left upper corner, we put x, y and also -1,
        # meaning it is starting point and i: index of our building. For right upper corner we put exactly the same,
        # but 1 instead of -1
        points  = [(l,y,-1,idx) for idx, (l,r,y) in enumerate(buildings)]
        points += [(r,y,1,idx) for idx, (l,r,y) in enumerate(buildings)]
        # Next, we sort our point by x coordinate. If it is equal, we sort them by height multiplied by -1 for left
        # point and by 1 for right point. Why so strange: the reason, that we first want to process starts,
        # from bigger to smaller, and then ends from smaller to bigger.
        points.sort(key = lambda x: (x[0], x[1]*x[2]))
        heap = [(0,-1)] # (-y,idx)
        active = {-1} # idx
        ans = [] # [x,y]

        for x, h, lr, idx in points:
            # Now, let us iterate through our points and: if we meet beginning of some building, we add it to active
            # set, if we meet end, we remove it from active set
            if lr == -1: active.add(idx)
            else: active.remove(idx)
            # If we meet left corner of building and also it is higher than we alredy met so far, that is
            # h > -heap[0][0], then we add this element to ans. Also we add (-h, ind) to our heap.
            if lr == -1:
                if h > -heap[0][0]:
                    ans.append([x, h])
                heappush(heap, (-h, idx))
            else:
                if h == -heap[0][0]:
                    # lazy updates
                    while heap and heap[0][1] not in active: heappop(heap)
                if -heap[0][0] != ans[-1][1]: # not overshadowed by a taller building
                    ans.append([x, -heap[0][0]])

        return ans
class tester(unittest.TestCase):
    def test1(self):
        buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        Output= [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        self.assertEqual(Output,Solution().getSkyline(buildings))
    def test2(self):
        buildings = [[2,9,10],[3,7,15],[5,12,12]]
        Output= [[2,10],[3,15],[7,12],[12,0]]
        self.assertEqual(Output,Solution().getSkyline(buildings))

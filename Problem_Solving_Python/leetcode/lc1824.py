from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# ERROR
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        di = {}
        def helper(cur_lane,i):
            if i==len(obstacles)-1:
                return 0
            if obstacles[i]==cur_lane:return float('inf')
            if (cur_lane,i) in di: return di[(cur_lane,i)] 
            if obstacles[i+1]==cur_lane:
                if obstacles[i+1]==1:
                    minn = 1 + min(helper(2,i),helper(3,i))
                elif obstacles[i+1]==2:
                    minn = 1 + min(helper(3,i),helper(1,i))
                else: # obstacles[i]==3:
                    minn = 1 + min(helper(1,i),helper(2,i))
            else:
                minn = helper(cur_lane,i+1)
            di[(cur_lane,i)] = minn
            return minn

        return helper(2,0)

class MyTestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2,Solution().minSideJumps([0,1,2,3,0]))
    def test_2(self):
        self.assertEqual(0,Solution().minSideJumps([0,1,1,3,3,0]))
    def test_3(self):
        self.assertEqual(2,Solution().minSideJumps([0,2,1,0,3,0]))
    def test_4(self):
        self.assertEqual(2,Solution().minSideJumps([0,2,0,0,0,3,0]))
        # for new_lane in [1,2,3]:
        #     if cur_lane == new_lane:continue
        #     minn= min(minn,helper(new_lane,i+1))

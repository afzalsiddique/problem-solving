import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        if n==1: return 0
        pq=[]
        for i in range(n):
            if i==n-1: break # reached last building
            diff = heights[i+1]-heights[i]
            if diff<=0: continue
            heappush(pq,(-diff,i))
            if bricks-diff<0 and ladders: # not enough bricks but have ladder
                tmp,idx=heappop(pq)
                tmp*=(-1)
                bricks+=tmp
                ladders-=1
            if bricks>=diff:
                bricks-=diff
            else: break
        # if heights[i]>=heights[i+1]: i+=1
        return i



class tester(unittest.TestCase):
    def test_1(self):
        heights = [4,2,7,6,9,14,12]
        bricks = 5
        ladders = 1
        Output= 4
        self.assertEqual(Output,get_sol().furthestBuilding(heights,bricks,ladders))
    def test_2(self):
        heights = [4,12,2,7,3,18,20,3,19]
        bricks = 10
        ladders = 2
        Output= 7
        self.assertEqual(Output,get_sol().furthestBuilding(heights,bricks,ladders))
    def test_3(self):
        heights = [14,3,19,3]
        bricks = 17
        ladders = 0
        Output= 3
        self.assertEqual(Output,get_sol().furthestBuilding(heights,bricks,ladders))
    def test_4(self):
        heights = [3,19]
        bricks = 87
        ladders = 1
        Output= 1
        self.assertEqual(Output,get_sol().furthestBuilding(heights,bricks,ladders))
    # def test_5(self):
    # def test_6(self):

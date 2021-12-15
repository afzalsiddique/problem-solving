import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/video-stitching/discuss/270680/C++-O(N)-No-Sorting-(Greedy)-Explained/442571
    def videoStitching(self, clips: List[List[int]], t: int) -> int:
        ends = [0] * (t + 1)
        for s, e in clips:
            if s <= t:
                ends[s] = max(ends[s], min(e, t)) # max reachable end
        i = count = furthest = currEnd = 0
        while currEnd < t:
            while i <= currEnd:
                furthest = max(furthest, ends[i])
                i += 1
            if furthest == currEnd:
                return -1
            currEnd = furthest
            count += 1
        return count

class Solution4:
    def videoStitching(self, clips: List[List[int]], t: int) -> int:
        max_right=[0]*(t+1)
        for l,r in clips:
            if l<t:
                max_right[l]=max(max_right[l],min(r,t)-l)
        return self.jump(max_right)

    def jump(self, nums: List[int]) -> int:
        # leetcode 45
        pos = len(nums)-1
        steps=0
        while pos:
            new_pos=pos
            for i in range(pos):
                if nums[i]+i>=pos:
                    new_pos=i
                    steps+=1
                    break
            if pos==new_pos: return -1
            pos=new_pos
        return steps
class Solution2:
    def videoStitching(self, clips: List[List[int]], t: int) -> int:
        max_right=[0]*(t+1) # "(t+1)" because [0,t] both are inclusive
        for l,r in clips:
            if l<t:
                max_right[l]=max(max_right[l],min(r,t))
        return self.jump(max_right)

    def jump(self, nums: List[int]) -> int:
        # leetcode 45
        pos = len(nums)-1
        steps=0
        while pos:
            new_pos=pos
            for i in range(pos):
                if nums[i]>=pos:
                    new_pos=i
                    steps+=1
                    break
            if pos==new_pos: return -1
            pos=new_pos
        return steps
class Solution3:
    # similar to jump game 2
    def videoStitching(self, clips: List[List[int]], t: int) -> int:
        max_jumps = [0]*101
        for l,r in clips:
            max_jumps[l] = max(max_jumps[l], r)

        # it is then a jump game
        res = lo = hi = 0
        while hi < t:
            lo, hi = hi, max(max_jumps[lo:hi+1])
            if hi <= lo: return -1
            res += 1
        return res

class tester(unittest.TestCase):
    def test_1(self):
        clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
        time = 10
        Output= 3
        self.assertEqual(Output,get_sol().videoStitching(clips,time))
    def test_2(self):
        clips = [[0,1],[1,2]]
        time = 5
        Output= -1
        self.assertEqual(Output,get_sol().videoStitching(clips,time))
    def test_3(self):
        clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
        time = 9
        Output= 3
        self.assertEqual(Output,get_sol().videoStitching(clips,time))
    def test_4(self):
        clips = [[0,4],[2,8]]
        time = 5
        Output= 2
        self.assertEqual(Output,get_sol().videoStitching(clips,time))
    # def test_5(self):
    # def test_6(self):
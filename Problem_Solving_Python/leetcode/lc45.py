import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
class Solution:
    # greedy
    # https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution/237098
    # start position from the end
    # Find the leftmost position that can reach the current position.
    def jump(self, nums: List[int]) -> int:
        pos = len(nums)-1
        steps=0
        while pos:
            new_pos=pos
            for i in range(pos):
                if nums[i]+i>=pos:
                    new_pos=i
                    steps+=1
                    break
            if pos==new_pos: return -1 # not required
            pos=new_pos
        return steps
class Solution2:
    def jump(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i):
            if i>=len(nums)-1: return 0
            res=float('inf')
            for jump in range(1,nums[i]+1):
                res=min(res,dfs(i+jump))
            return res+1

        return dfs(0)


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().jump([2,3,1,1,4]))
    def test_2(self):
        self.assertEqual(2, Solution().jump([2,3,0,1,4]))
    def test_3(self):
        self.assertEqual(1, Solution().jump([2,1]))

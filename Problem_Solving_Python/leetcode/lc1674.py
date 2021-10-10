import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-moves-to-make-array-complementary/discuss/953078/Prefix-sum-O(n-%2B-limit)-with-detailed-examples-and-pseudocode
    def minMoves(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        line_sweep = [0]*(2*limit+2)
        for i in range(n//2):
            a,b=nums[i],nums[n-1-i]
            line_sweep[2]+=2
            line_sweep[min(a,b)+1]-=1
            line_sweep[a+b]-=1
            line_sweep[a+b+1]+=1
            line_sweep[max(a,b)+limit+1]+=1
        line_sweep = list(itertools.accumulate(line_sweep))
        line_sweep[0]=float('inf') # invalid case
        line_sweep[1]=float('inf') # invalid case
        return min(line_sweep)


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,limit = [1,2,4,3],  4
        Output= 1
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    def test2(self):
        nums,limit = [1,2,2,1],  2
        Output= 2
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    def test3(self):
        nums,limit = [1,2,1,2],  2
        Output= 0
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    def test4(self):
        nums,limit = [1,2,4,3,6,5,5,6,3,4,2,3],  6
        Output= 5
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    def test5(self):
        nums,limit = [3,5],  7
        Output= 0
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    def test6(self):
        nums,limit = [1,3,1,1,1,2,3,2,3,1,3,2,1,3], 3
        Output= 4
        self.assertEqual(Output, get_sol().minMoves(nums,limit))
    # def test7(self):

from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
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
        @cache
        def dfs(i):
            if i>=len(nums)-1: return 0
            res=float('inf')
            for jump in range(1,nums[i]+1):
                res=min(res,dfs(i+jump))
            return res+1

        return dfs(0)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().jump([2,3,1,1,4]))
    def test02(self):
        self.assertEqual(2, get_sol().jump([2,3,0,1,4]))
    def test03(self):
        self.assertEqual(1, get_sol().jump([2,1]))
    def test04(self):
        self.assertEqual(0, get_sol().jump([0]))
    def test05(self):
        self.assertEqual(3, get_sol().jump([1,2,1,1,1]))
    def test06(self):
        self.assertEqual(2, get_sol().jump([4,1,1,3,1,1,1]))

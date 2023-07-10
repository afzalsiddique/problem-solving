from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # O(n)
    # greedy bfs
    # https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        res=curEnd=maxEnd=0
        for i in range(n-1):
            maxEnd=max(maxEnd,i+nums[i])
            if i==curEnd:
                res+=1
                curEnd=maxEnd

        return res
class Solution2:
    # time O(n^2) although the post says O(n)
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
class Solution3:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i>=len(nums)-1: return 0
            res=float('inf')
            for jump in range(1,nums[i]+1):
                res=min(res,1+dfs(i+jump))
            return res

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
    def test07(self):
        self.assertEqual(5, get_sol().jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
    def test08(self):
        self.assertEqual(13, get_sol().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))

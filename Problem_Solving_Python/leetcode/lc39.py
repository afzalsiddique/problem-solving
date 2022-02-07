from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,n= [],len(candidates)

        def dfs(start, target, path):
            if target==0:
                res.append(path)
                return
            if target<0:return
            for i in range(start, n):
                dfs(i, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        dfs(0, target, [])
        return res

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # version 2
        li = []
        n = len(candidates)
        combination = []
        candidates.sort()

        def helper(start, summ):
            if summ == target:
                li.append(combination[:])
                return

            if summ > target:
                return

            for i in range(start, n):
                combination.append(candidates[i])
                helper(i, summ+candidates[i])
                combination.pop(-1)

        helper(0,0)
        return li


class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = sorted(get_sol().combinationSum([2,3,6,7], 7))
        expected = sorted([[2,2,3],[7]])
        self.assertEqual(expected, actual)
    def test_2(self):
        actual = sorted(get_sol().combinationSum([2,3,5], 8))
        expected = sorted([[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = sorted(get_sol().combinationSum([2], 1))
        expected = sorted([])
        self.assertEqual(expected, actual)
    def test_4  (self):
        actual = sorted(get_sol().combinationSum([1], 1))
        expected = sorted([[1]])
        self.assertEqual(expected, actual)
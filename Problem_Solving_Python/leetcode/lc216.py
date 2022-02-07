from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()



# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res  = []

        def dfs(target, start, path):
            if len(path)==k:
                if target==0:
                    res.append(path)
                return
            if target<0:return

            for i in range(start, 9+1):
                dfs(target-i, i+1, path+[i])

        dfs(target, 1, [])
        return res

class Solution2:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        # similar
        res, comb = [], []

        def helper(start, depth, summ):
            if depth > k:
                return
            if summ == target and depth==k:
                res.append(comb[:])
                return

            for i in range(start, 9+1):
                comb.append(i)
                helper(i + 1, depth + 1, summ + i)
                comb.pop(-1)

        helper(1, 0, 0)
        return res


class MyTestCase(unittest.TestCase):

    def test01(self):
        self.assertEqual([[1,2,4]], get_sol().combinationSum3(3, 7))
    def test02(self):
        self.assertEqual([[1,2,6],[1,3,5],[2,3,4]], get_sol().combinationSum3(3, 9))
    def test03(self):
        self.assertEqual([], get_sol().combinationSum3(4, 1))
    def test04(self):
        self.assertEqual([], get_sol().combinationSum3(3, 2))
    def test05(self):
        self.assertEqual([[1,2,3,4,5,6,7,8,9]], get_sol().combinationSum3(9, 45))
from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum-ii/discuss/16878/Combination-Sum-I-II-and-III-Java-solution-(see-the-similarities-yourself)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,n= [],len(candidates)

        def dfs(target, start, path):
            if target==0:
                res.append(path)
                return
            if target<0:return
            for i in range(start, n):
                if i>start and candidates[i]==candidates[i-1]:continue
                # if i>0 and candidates[i]==candidates[i-1]:continue # wrong
                dfs(target-candidates[i], i+1, path+[candidates[i]])

        candidates.sort()
        dfs(target,0,[])
        return res
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # version 2
        res,path, n = [],[],len(candidates)
        candidates.sort()

        def helper(start, summ):
            if summ == target:
                res.append(path[:])
                return

            if summ > target:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, summ + candidates[i])
                path.pop(-1)

        helper(0,0)
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual = sorted(get_sol().combinationSum2([10,1,2,7,6,1,5], 8))
        expected = sorted([ [1,1,6], [1,2,5], [1,7], [2,6] ])
        self.assertEqual(expected, actual)

    def test_2(self):
        actual = sorted(get_sol().combinationSum2([2,5,2,1,2], 5))
        expected = sorted([ [1,2,2], [5] ])
        self.assertEqual(expected, actual)
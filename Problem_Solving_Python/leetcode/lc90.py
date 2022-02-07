from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums),[]

        def dfs(start, path):
            res.append(path)

            for i in range(start, n):
                if i>start and nums[i]==nums[i-1]:continue
                dfs(i+1, path+[nums[i]])

        nums.sort()
        dfs(0,[])
        return res
class Solution2:
    # similar but with one less parameter
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, res, comb = len(nums), [], []

        def backtrack(start):
            res.append(comb[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                comb.append(nums[i])
                backtrack(i + 1)
                comb.pop(-1)

        nums.sort() # if not sorted duplicates will not be together
        backtrack(0)
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        actual = sorted(get_sol().subsetsWithDup([1, 2, 2]))
        expected = sorted([ [2], [1], [1, 2, 2], [2, 2], [1, 2], [] ])
        self.assertEqual(expected, actual)

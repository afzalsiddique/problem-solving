from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        di, n = {}, len(nums)

        def dfs(target):
            if target==0:return 1
            if target<0: return 0
            if target in di:return di[target]
            ans = 0
            for i in range(n):
                ans += dfs(target-nums[i])
            di[target] = ans
            return ans

        return dfs(target)



class MyTestCase(unittest.TestCase):

    def test01(self):
        nums = [1,2,3]
        target = 4
        actual = get_sol().combinationSum4(nums, target)
        expected = 7
        self.assertEqual(expected, actual)
    def test02(self):
        nums = [4,2,1]
        target = 32
        actual = get_sol().combinationSum4(nums, target)
        expected = 39882198
        self.assertEqual(expected, actual)

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
class Solution2:
    # greedy
    # time O(n^2)
    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/478708/RZ-Summary-of-all-the-solutions-I-have-learned-from-Discuss-in-Python
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            index = arr.index(min(arr))
            if index==0: # first one. only one neighbor
                res+=arr[index] * arr[index+1]
            elif index==len(arr)-1: # last one. only one neighbor
                res+=arr[index]*arr[index-1]
            else:
                res += arr[index] * min(arr[index - 1], arr[index + 1])
            arr.pop(index)
        return res
class Solution3:
    # dp
    # time O(n^3)
    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/478708/RZ-Summary-of-all-the-solutions-I-have-learned-from-Discuss-in-Python
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = {}
        def helper(l, r):
            if l >= r: return 0
            if (l, r) in dp: return dp[l, r]

            res = float('inf')
            for i in range(l, r):
                rootVal = max(arr[l:i+1]) * max(arr[i+1:r+1])
                res = min(res, rootVal + helper(l, i) + helper(i + 1, r))

            dp[l, r] = res
            return res

        return helper(0, len(arr) - 1)


class tester(unittest.TestCase):
    def test1(self):
        arr = [6,2,4]
        Output= 32
        self.assertEqual(Output,get_sol().mctFromLeafValues(arr))

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/binary-trees-with-factors/discuss/1107208/Python-Short-O(n2)-solution-explained
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        sett=set(arr)
        dp={}
        def helper(root):
            if root in dp: return dp[root]
            ans=1
            for x in sett:
                if root%x==0 and root//x in sett:
                    ans+=helper(x)*helper(root//x)
            dp[root]=ans
            return ans

        res=0
        for x in sett:
            res+=helper(x)
            res%=10**9+7
        return res

class tester(unittest.TestCase):
    def test_1(self):
        arr = [2,4]
        Output= 3
        self.assertEqual(Output,get_sol().numFactoredBinaryTrees(arr))
    def test_2(self):
        arr = [2,4,5,10]
        Output= 7
        self.assertEqual(Output,get_sol().numFactoredBinaryTrees(arr))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):

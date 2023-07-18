from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize

def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[Counter() for _ in range(n)] # dp[i][d] denotes the number of arithmetic subsequences that ends with A[i] and its common difference is d
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=dp[j][diff]+1
        res=sum(sum(dp[i].values()) for i in range(n))
        return res-(n*(n-1)//2)




class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,Solution().numberOfArithmeticSlices(nums = [2,4,6,8]))
    def test2(self):
        self.assertEqual(7,Solution().numberOfArithmeticSlices(nums = [2,4,6,8,10]))
    def test3(self):
        self.assertEqual(1,Solution().numberOfArithmeticSlices(nums = [7,7,7]))
    def test4(self):
        self.assertEqual(5,Solution().numberOfArithmeticSlices(nums = [7,7,7,7]))
    def test5(self):
        self.assertEqual(16,Solution().numberOfArithmeticSlices(nums = [7,7,7,7,7]))
    def test6(self):
        self.assertEqual(42,Solution().numberOfArithmeticSlices(nums = [7,7,7,7,7,7]))
    def test7(self):
        self.assertEqual(8,Solution().numberOfArithmeticSlices(nums = [2,4,6,8,7,7,7,7]))
    def test8(self):
        self.assertEqual(9,Solution().numberOfArithmeticSlices(nums = [2,7,4,7,6,7,8,7]))
    def test9(self):
        self.assertEqual(0,Solution().numberOfArithmeticSlices(nums = [0,2000000000,-294967296]))

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/smallest-range-ii/discuss/980294/Python-O(n-log-n)-solution-explained/875149
    def smallestRangeII(self, A: List[int], k: int) -> int:
        n=len(A)
        # if n==1: return 0
        A.sort()
        res=A[-1]-A[0]
        for i in range(n - 1):
            tmp = [A[0]+k, A[i]+k, A[i+1]-k, A[-1]-k]
            res = min(res,max(tmp)-min(tmp))
        return res

class tester(unittest.TestCase):
    def test_1(self):
        nums = [1]
        k = 0
        Output= 0
        self.assertEqual(Output, get_sol().smallestRangeII(nums,k))
    def test_2(self):
        nums = [0,10]
        k = 2
        Output= 6
        self.assertEqual(Output, get_sol().smallestRangeII(nums,k))
    def test_3(self):
        nums,k = [1,3,6], 3
        Output= 3
        self.assertEqual(Output, get_sol().smallestRangeII(nums,k))
    def test_4(self):
        nums,k = [7,8,8], 5
        Output= 1
        self.assertEqual(Output, get_sol().smallestRangeII(nums,k))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/make-sum-divisible-by-p/discuss/854197/JavaC%2B%2BPython-Prefix-Sum
    # Here "curr" represents the sum of remainders of (0 to i) and "want" represent sum of remainders from (o to lets
    # say some index j) and "need" is the sum of remainders from i to j. So curr - want = need which implies curr -
    # need is what we want to look in the last remainders that we stored.
    # For any number N, where X,Y and Z < N such that (X + Y) % N = Z
    # X = (Z - Y + N) % N
    # Y = (Z - X + N) % N
    # So, Z=curr, X=need/want, Y=need/want
    # that's why want=(need-curr)% p is wrong
    def minSubarray(self, A: List[int], p: int) -> int:
        n=len(A)
        need=sum(A)%p
        if need==0: return 0
        di={0:-1}
        curr=0
        res=float('inf')
        for i,a in enumerate(A):
            curr= (curr+a)%p
            want=(curr-need)%p
            # want = (need-curr)%p # WRONG
            if want in di:
                res=min(res,i-di[want])
            di[curr]=i
        return res if res<n else -1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,p = [3,1,4,2],6
        Output= 1
        self.assertEqual(Output, get_sol().minSubarray(nums,p))
    def test_2(self):
        nums,p = [6,3,5,2],9
        Output= 2
        self.assertEqual(Output, get_sol().minSubarray(nums,p))
    def test_3(self):
        nums,p = [1,2,3],3
        Output= 0
        self.assertEqual(Output, get_sol().minSubarray(nums,p))
    def test_4(self):
        nums,p = [1,2,3],7
        Output= -1
        self.assertEqual(Output, get_sol().minSubarray(nums,p))
    def test_5(self):
        nums,p = [1000000000,1000000000,1000000000],3
        Output= 0
        self.assertEqual(Output, get_sol().minSubarray(nums,p))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
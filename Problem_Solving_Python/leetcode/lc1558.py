import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/805740/JavaC%2B%2BPython-Bit-Counts
    def minOperations(self, A: List[int]) -> int:
        def no_op0(a:int):
            tmp=bin(a)
            cnt=0
            for x in tmp:
                if x=='1':
                    cnt+=1
            return cnt
        def no_op1(a:int):
            tmp=bin(a)[2:]
            return len(tmp)-1
        return sum(no_op0(a) for a in A) + max(no_op1(a) for a in A)
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,5]
        Output= 5
        self.assertEqual(Output, get_sol().minOperations(nums))
    def test_2(self):
        nums = [2,2]
        Output= 3
        self.assertEqual(Output, get_sol().minOperations(nums))
    def test_3(self):
        nums = [4,2,5]
        Output= 6
        self.assertEqual(Output, get_sol().minOperations(nums))
    def test_4(self):
        nums = [3,2,2,4]
        Output= 7
        self.assertEqual(Output, get_sol().minOperations(nums))
    def test_5(self):
        nums = [2,4,8,16]
        Output= 8
        self.assertEqual(Output, get_sol().minOperations(nums))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
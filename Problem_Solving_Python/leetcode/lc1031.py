import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n=len(nums)
        pre_sum=[nums[0]]
        for i in range(1,n):
            pre_sum.append(pre_sum[-1]+nums[i])

        maxx=0
        for i in range(firstLen-1,n):
            if i-firstLen>=0:
                a = pre_sum[i]-pre_sum[i-firstLen]
            else:
                a = pre_sum[i]
            for j in range(i+1,n):
                if j-secondLen<i: continue # must non overlapping
                if j-secondLen>=0:
                    b=pre_sum[j]-pre_sum[j-secondLen]
                else:
                    b=pre_sum[j]
                maxx=max(maxx,a+b)

        for i in range(secondLen-1,n):
            if i-secondLen>=0:
                a = pre_sum[i]-pre_sum[i-secondLen]
            else:
                a = pre_sum[i]
            for j in range(i+1,n):
                if j-firstLen<i: continue # must non overlapping
                if j-firstLen>=0:
                    b=pre_sum[j]-pre_sum[j-firstLen]
                else:
                    b=pre_sum[j]
                maxx=max(maxx,a+b)

        return maxx

class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums = [0,6,5,2,2,5,1,9,4]
        firstLen = 1
        secondLen = 2
        Output= 20
        self.assertEqual(Output,get_sol().maxSumTwoNoOverlap(nums,firstLen,secondLen))
    def test_02(self):
        nums = [3,8,1,3,2,1,8,9,0]
        firstLen = 3
        secondLen = 2
        Output= 29
        self.assertEqual(Output,get_sol().maxSumTwoNoOverlap(nums,firstLen,secondLen))
    def test_03(self):
        nums = [2,1,5,6,0,9,5,0,3,8]
        firstLen = 4
        secondLen = 3
        Output= 31
        self.assertEqual(Output,get_sol().maxSumTwoNoOverlap(nums,firstLen,secondLen))
    def test_04(self):
        nums = [1,0,3]
        firstLen = 1
        secondLen = 2
        Output= 4
        self.assertEqual(Output,get_sol().maxSumTwoNoOverlap(nums,firstLen,secondLen))
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):

import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        nums=[0]+nums+[0]
        n=len(nums)
        odd_pre=[0]
        for i in range(1,n):
            odd_pre.append(odd_pre[-1]+nums[i] if i&1 else odd_pre[-1])
        even_pre=[nums[0]]
        for i in range(1,n):
            even_pre.append(even_pre[-1]+nums[i] if not i&1 else even_pre[-1])

        cnt=0
        for i in range(1,n-1):
            # x=odd_pre[i-1]+even_pre[n-1]-even_pre[i]
            # y=even_pre[i-1]+odd_pre[n-1]-odd_pre[i]
            if odd_pre[i-1]+even_pre[n-1]-even_pre[i]==even_pre[i-1]+odd_pre[n-1]-odd_pre[i]:
                cnt+=1
        return cnt
class Solution2:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n=len(nums)
        odd_pre=[0]
        for i in range(1,n):
            if i&1:
                odd_pre.append(odd_pre[-1]+nums[i])
            else:
                odd_pre.append(odd_pre[-1])
        even_pre=[nums[0]]
        for i in range(1,n):
            if not i&1:
                even_pre.append(even_pre[-1]+nums[i])
            else:
                even_pre.append(even_pre[-1])
        # print(even_pre)
        # print(odd_pre)

        cnt=0
        for i in range(n):
            if i==0:
                if odd_pre[n-1]-odd_pre[i]==even_pre[n-1]-even_pre[i]:
                    cnt+=1
            elif i==n-1:
                if odd_pre[i-1]==even_pre[i-1]:
                    cnt+=1
            elif odd_pre[i-1]+even_pre[n-1]-even_pre[i]==even_pre[i-1]+odd_pre[n-1]-odd_pre[i]:
                cnt+=1
            # print(odd_pre[i-1]+even_pre[n-1]-even_pre[i])
            # print(even_pre[i-1]+odd_pre[n-1]-odd_pre[i])
        return cnt


class Tester(unittest.TestCase):
    def test_1(self):
        nums = [2,1,6,4]
        Output= 1
        self.assertEqual(Output,get_sol().waysToMakeFair(nums))
    def test_2(self):
        nums = [1,1,1]
        Output= 3
        self.assertEqual(Output,get_sol().waysToMakeFair(nums))
    def test_3(self):
        nums = [1,2,3]
        Output= 0
        self.assertEqual(Output,get_sol().waysToMakeFair(nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        def h(A:List[int]):
            n=len(A)
            res=0
            for i in range(0,n-2,2):
                minn=min(A[i],A[i+2])
                if A[i+1]>=minn:
                    res+=A[i+1]-minn+1
            if not n&1:
                if A[-1]>=A[-2]:
                    res+=A[-1]-A[-2]+1
            return res

        n=len(A)
        if n==1 or n==2: return 0
        ans1=h(A)
        if A[0]>=A[1]:
            ans2=h(A[1:]) + A[0]-A[1]+1
        else:
            ans2=h(A[1:])
        return min(ans1,ans2)
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3]
        Output= 2
        self.assertEqual(Output, get_sol().movesToMakeZigzag(nums))
    def test_2(self):
        nums = [9,6,1,6,2]
        Output= 4
        self.assertEqual(Output, get_sol().movesToMakeZigzag(nums))
    def test_3(self):
        nums = [1,2,1,2]
        Output= 0
        self.assertEqual(Output, get_sol().movesToMakeZigzag(nums))
    def test_4(self):
        nums = [2,7,10,9,8,9]
        Output= 4
        self.assertEqual(Output, get_sol().movesToMakeZigzag(nums))
    def test_5(self):
        nums = [1]
        Output= 0
        self.assertEqual(Output, get_sol().movesToMakeZigzag(nums))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

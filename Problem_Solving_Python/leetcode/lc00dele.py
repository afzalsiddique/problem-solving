import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        n=len(A)
        l,r=0,0
        di=defaultdict(int)
        maxx=0
        cur=0
        while r<n:
            if di[A[r]]==0:
                di[A[r]]+=1
                cur+=A[r]
                r+=1
                maxx=max(maxx,cur)
            else:
                di[A[l]]-=1
                cur-=A[l]
                l+=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [4,2,4,5,6]
        Output= 17
        self.assertEqual(Output, get_sol().maximumUniqueSubarray(nums))
    def test_2(self):
        nums = [5,2,1,2,5,2,1,2,5]
        Output= 8
        self.assertEqual(Output, get_sol().maximumUniqueSubarray(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

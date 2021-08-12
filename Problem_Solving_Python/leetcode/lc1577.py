import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        def f(A:List[int], B:List[int]):
            res=0
            di=defaultdict(int)
            for i in range(len(A)):
                for j in range(i):
                    di[A[i]*A[j]]+=1
            for x in B:
                res+=di[x*x]
            return res

        return f(A,B) + f(B,A)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums1,nums2 = [7,4], [5,2,8,9]
        Output= 1
        self.assertEqual(Output, get_sol().numTriplets(nums1,nums2))
    def test_2(self):
        nums1,nums2 = [1,1], [1,1,1]
        Output= 9
        self.assertEqual(Output, get_sol().numTriplets(nums1,nums2))
    def test_3(self):
        nums1,nums2 = [7,7,8,3], [1,2,9,7]
        Output= 2
        self.assertEqual(Output, get_sol().numTriplets(nums1,nums2))
    def test_4(self):
        nums1,nums2 = [4,7,9,11,23], [3,5,1024,12,18]
        Output= 0
        self.assertEqual(Output, get_sol().numTriplets(nums1,nums2))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
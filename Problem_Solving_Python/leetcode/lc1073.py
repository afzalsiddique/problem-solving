import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def decimal_to_base_neg2(self,a:int)->List[int]:
        if a==0: return [0]
        res=[]
        while a:
            res.append(a&1)
            a = -(a//2)
        return res[::-1]
    def addNegabinary(self, A: List[int], B: List[int]) -> List[int]:
        powers=[1]
        for i in range(1001): powers.append(powers[-1]*(-2))
        a=0
        A=A[::-1]
        for i in range(len(A)):
            a+= A[i]*powers[i]
        b=0
        B=B[::-1]
        for i in range(len(B)):
            b+= B[i]*powers[i]
        return self.decimal_to_base_neg2(a+b)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr1,arr2 = [1,1,1,1,1],[1,0,1]
        Output= [1,0,0,0,0]
        self.assertEqual(Output, get_sol().addNegabinary(arr1,arr2))
    def test_2(self):
        arr1,arr2 = [0],[0]
        Output= [0]
        self.assertEqual(Output, get_sol().addNegabinary(arr1,arr2))
    def test_3(self):
        arr1,arr2 = [0],[1]
        Output= [1]
        self.assertEqual(Output, get_sol().addNegabinary(arr1,arr2))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # see the solution below for better understanding
    def tupleSameProduct(self, A: List[int]) -> int:
        n=len(A)
        freq=Counter(); res=0
        for i in range(n):
            for j in range(i):
                prod = A[i]*A[j]
                res+= 8 * freq[prod]
                freq[prod]+=1
        return res
class Solution2:
    def tupleSameProduct(self, A: List[int]) -> int:
        def nC2(n): return n*(n-1)//2 # no of ways to choose 2 items out of n items
        n=len(A)
        freq=Counter(); res=0
        for i in range(n):
            for j in range(i):
                freq[A[i]*A[j]]+=1
        for prod in freq:
            res+= 8* nC2(freq[prod])
        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        A = [2,3,4,6]
        Output= 8
        self.assertEqual(Output, get_sol().tupleSameProduct(A))
    def test_2(self):
        A = [1,2,4,5,10]
        Output= 16
        self.assertEqual(Output, get_sol().tupleSameProduct(A))
    def test_3(self):
        A = [2,3,5,7]
        Output= 0
        self.assertEqual(Output, get_sol().tupleSameProduct(A))
    def test_4(self):
        A = [2,3,4,6,8,12]
        Output= 40
        self.assertEqual(Output, get_sol().tupleSameProduct(A))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
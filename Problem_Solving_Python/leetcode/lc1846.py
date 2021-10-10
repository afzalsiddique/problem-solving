import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n=len(arr)
        arr.sort()
        arr[0]=1
        for i in range(1,n):
            if arr[i]-arr[i-1]>1:
                arr[i]=arr[i-1]+1
        return arr[-1]

class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [2,2,1,2,1]
        Output= 2
        self.assertEqual(Output, get_sol().maximumElementAfterDecrementingAndRearranging(arr))
    def test2(self):
        arr = [100,1,1000]
        Output= 3
        self.assertEqual(Output, get_sol().maximumElementAfterDecrementingAndRearranging(arr))
    def test3(self):
        arr = [1,2,3,4,5]
        Output= 5
        self.assertEqual(Output, get_sol().maximumElementAfterDecrementingAndRearranging(arr))
    def test4(self):
        arr = [73,98,9]
        Output= 3
        self.assertEqual(Output, get_sol().maximumElementAfterDecrementingAndRearranging(arr))
    # def test5(self):
    # def test6(self):
    # def test7(self):

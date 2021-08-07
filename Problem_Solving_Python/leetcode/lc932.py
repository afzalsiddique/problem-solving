import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/beautiful-array/discuss/186679/
    # https://leetcode.com/problems/beautiful-array/discuss/186901/JavaScript-How-I-understand-the-solution-(with-verification-of-the-solution)
    def beautifulArray(self, n: int) -> List[int]:
        def f(arr):
            if len(arr)>n: return arr
            res=[]
            for x in arr: res.append(x*2-1)
            for x in arr: res.append(x*2)
            return f(res)

        arr=[1]
        res=f(arr)
        res=[x for x in res if x<=n]
        return res

class Tester(unittest.TestCase):
    def valid(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(i+1,j):
                    if arr[k]*2==arr[i]+arr[j]:
                        return False
        return True
    def test_1(self):
        n = 4
        res =get_sol().beautifulArray(n)
        print(res)
        self.assertEqual(True,Tester().valid(res))
    def test_2(self):
        n = 5
        res =get_sol().beautifulArray(n)
        print(res)
        self.assertEqual(True,Tester().valid(res))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def possible(mid):
            total=0
            for i in range(1,m+1): # for every row
                total+=(min(mid,i*n))//i
            return total<k

        lo,hi=0,m*n+1
        while lo<=hi:
            mid=(lo+hi)//2
            if possible(mid):
                lo=mid+1
            else:
                hi=mid-1
        return lo
class Solution2:
    # https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/discuss/1580882/Python-Binary-search-solution-explained/1152080
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def hasLessOrEq(x): # has at least k no of elements which are less than or equal to x
            res=0
            for i in range(1,n+1): # for each col
                res+=min(x//i,m) # How many numbers are less than or equal to x in that col. add those numbers
            return res>=k

        lo,hi=0,m*n
        while lo<=hi:
            mid=(lo+hi)//2
            if hasLessOrEq(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().findKthNumber(m = 3, n = 3, k = 5))
    def test02(self):
        self.assertEqual(6, get_sol().findKthNumber(m = 2, n = 3, k = 6))
    def test03(self):
        self.assertEqual(312, get_sol().findKthNumber(45, 12, 471))
    def test04(self):
        self.assertEqual(31666344, get_sol().findKthNumber(9895, 28405, 100787757))
    # def test05(self):
    # def test06(self):
    # def test07(self):

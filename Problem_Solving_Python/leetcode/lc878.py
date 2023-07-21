import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a,b):
            if a>b:
                return gcd(b,a)
            if a==0:
                return b
            return gcd(b%a,a)

        def getLCM(a,b):
            tmp=gcd(a,b)
            return int(a*b/tmp)
        def lessThan(x):
            ans1=x//a
            ans2=x//b
            ans3=x//lcm
            return ans1+ans2-ans3<n

        MOD=10**9+7
        lcm=getLCM(a,b)
        beg,end=0,n*min(a,b)
        while beg<=end:
            mid=(beg+end)//2
            if lessThan(mid):
                beg=mid+1
            else:
                end=mid-1
        return beg % MOD

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().nthMagicalNumber(1,2,3))
    def test02(self):
        self.assertEqual(6, get_sol().nthMagicalNumber(4,2,3))
    def test03(self):
        self.assertEqual(999720007, get_sol().nthMagicalNumber(1000000000, 40000, 40000))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):

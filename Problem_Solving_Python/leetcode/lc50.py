from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # extended problem where we have return the mod instead of actual answer
    # I am not 100% sure about the implementation
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n,MOD=10**9+7):
            if x<0: # remove this part if x>=0
                if n%2:
                    return (-1)*helper(-x,n)
                return helper(-x,n)
            if n<0: return 1/helper(x,-n)
            if n==0: return 1
            if n==1: return x
            prod=helper(x,n//2)%MOD
            prod=(prod*prod)%MOD
            if n%2:
                return (prod*x) % MOD
            return prod

        return helper(x,n)
class Solution2:
    # https://www.youtube.com/watch?v=snOaKR2xgZg
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n<0: return 1/helper(x,-n)
            if n==0: return 1
            if n==1: return x
            prod=helper(x,n//2)
            prod*=prod
            if n%2:
                return prod*x
            return prod

        return helper(x,n)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual( 4.00000, get_sol().myPow(2,2))
    def test_2(self):
        self.assertEqual( 16.00000, get_sol().myPow(2,4))
    def test_3(self):
        self.assertEqual( 128, get_sol().myPow(2,7))
    def test_4(self):
        self.assertEqual( 9.26100, get_sol().myPow(2.1, 3))
    def test_5(self):
        self.assertEqual( 0.25000, get_sol().myPow(2,-2))
    def test_6(self):
        self.assertEqual(54.83508, get_sol().myPow(0.44894, -5))
    def test_7(self):
        self.assertEqual(4.00, get_sol().myPow(-2.00000, 2))


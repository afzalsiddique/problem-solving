import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=IZMdNccsc-8
    def checkPowersOfThree(self, n: int) -> bool:
        BIG=15
        for i in range(BIG,-1,-1):
            x=pow(3,i)
            if x<=n:
                n-=x
            if n==0: return True
        return False
class Solution2:
    # tle
    def checkPowersOfThree(self, n: int) -> bool:
        def cub_root(x: int) -> int:
            if x == 0 or x == 1: return x
            l, r = 0, x
            while l <= r:
                mid = (l + r) // 2
                if mid * mid * mid == x:
                    return mid
                if mid * mid * mid <= x and (mid + 1) * (mid + 1) * (mid + 1) > x:
                    return mid
                if mid * mid * mid > x:
                    r = mid
                else:
                    l = mid
            return mid

        def power(x, n):
            if (n == 0):
                return 1
            temp = power(x, n // 2)
            if (n % 2 == 0):
                return temp * temp
            else:
                return x * temp * temp

        def helper(n, start):
            if n == 0: return True
            if n < 0: return False
            root = cub_root(n)
            for i in range(start, root + 1):
                if helper(n - power(3, i), i + 1):
                    return True
            return False

        return helper(n, 0)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 12
        Output= True
        self.assertEqual(Output, get_sol().checkPowersOfThree(n))
    def test_2(self):
        n = 91
        Output= True
        self.assertEqual(Output, get_sol().checkPowersOfThree(n))
    def test_3(self):
        n = 21
        Output= False
        self.assertEqual(Output, get_sol().checkPowersOfThree(n))
    def test_4(self):
        n = 2616799
        Output= False
        self.assertEqual(Output, get_sol().checkPowersOfThree(n))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        minus = (numerator>0 and denominator<0) or (numerator<0 and denominator>0)
        numerator,denominator=abs(numerator),abs(denominator)
        res = []

        i=0
        before_decimal = numerator//denominator
        res.append(str(before_decimal))
        i+=1
        res.append('.')
        i+=1

        remainder = numerator%denominator
        di = {}
        while remainder!=0 and remainder not in di:
            flag= False
            while remainder<denominator:
                flag=True
                di[remainder]=i
                res.append('0')
                remainder*=10
                i+=1
            if flag: res.pop()
            res.append(str(remainder//denominator))
            remainder = remainder%denominator

        if remainder in di: # pattern found
            start = di[remainder] # start of the pattern
            res = res[:start]+['(']+res[start:]+[')'] # add parenthesis around the pattern
        if res and res[-1]=='.': res.pop() # if nothing after decimal, remove decimal
        res = ''.join(res)
        return '-'+res if minus else res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual("0.5", get_sol().fractionToDecimal( 1,  2))
    def test02(self):
        self.assertEqual("2", get_sol().fractionToDecimal( 2,  1))
    def test03(self):
        self.assertEqual("0.(6)", get_sol().fractionToDecimal( 2,  3))
    def test04(self):
        self.assertEqual("0.(012)", get_sol().fractionToDecimal( 4,  333))
    def test05(self):
        self.assertEqual("0.2", get_sol().fractionToDecimal( 1,  5))
    def test06(self):
        self.assertEqual("-6.25", get_sol().fractionToDecimal( -50, 8))
    def test07(self):
        self.assertEqual("-2147483648", get_sol().fractionToDecimal( -2147483648, 1))
    def test08(self):
        self.assertEqual("0.1(6)", get_sol().fractionToDecimal( 1, 6))
    def test09(self):
        self.assertEqual("0", get_sol().fractionToDecimal( 0, -5))

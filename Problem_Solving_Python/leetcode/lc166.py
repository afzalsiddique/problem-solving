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
    def test1(self):
        numerator,denominator = 1,  2
        Output= "0.5"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test2(self):
        numerator,denominator = 2,  1
        Output= "2"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test3(self):
        numerator,denominator = 2,  3
        Output= "0.(6)"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test4(self):
        numerator,denominator = 4,  333
        Output= "0.(012)"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test5(self):
        numerator,denominator = 1,  5
        Output= "0.2"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test6(self):
        numerator,denominator = -50, 8
        Output= "-6.25"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test7(self):
        numerator,denominator = -2147483648, 1
        Output= "-2147483648"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))
    def test8(self):
        numerator,denominator = 1, 6
        Output= "0.1(6)"
        self.assertEqual(Output, get_sol().fractionToDecimal(numerator,denominator))

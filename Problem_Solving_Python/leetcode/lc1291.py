import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def gen(self,low,high,no_of_digits,res):
        for i in range(1,9+1):
            li=[]
            li.append(i)
            for j in range(1,no_of_digits):
                li.append(i+j)
            x=int(''.join(list(map(str,li)))) # convert the li to int x
            length = len(str(x)) # no of digits in int x
            if length==no_of_digits and low<=x<=high:
                res.append(x)

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=len(str(low))
        r=len(str(high))
        res=[]
        for no_of_digits in range(l,r+1):
            self.gen(low,high,no_of_digits,res)
        return res



class MyTestCase(unittest.TestCase):
    def test_01(self):
        low=1000
        high=9999
        no_of_digits=4
        res=[]
        Output=[1234,2345,3456,4567,5678,6789]
        get_sol().gen(low,high,no_of_digits,res)
        self.assertEqual(Output,res)
    def test_02(self):
        low = 100
        high = 300
        Output= [123,234]
        self.assertEqual(Output,get_sol().sequentialDigits(low,high))
    def test_03(self):
        low = 1000
        high = 13000
        Output= [1234,2345,3456,4567,5678,6789,12345]
        self.assertEqual(Output,get_sol().sequentialDigits(low,high))
    def test_04(self):
        low = 10
        high = 1000000000
        Output= [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        self.assertEqual(Output,get_sol().sequentialDigits(low,high))

    # def test_05(self):
    # def test_06(self):
    # def test_07(self):

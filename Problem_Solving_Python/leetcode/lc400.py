import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # there are 9 1 digit numbers -> 1-9
    # there are 90 2 digit numbers -> 10-99
    # there are 900 3 digit numbers -> 100-999

    # numbers upto 1 digit  = 9     -> 1-9
    # numbers upto 2 digits = 99    -> 1-99
    # numbers upto 3 digits = 999   -> 1-999

    # spaces upto 1 digit  = 9*1
    # spaces upto 2 digits = 9*1 + 90*2
    # spaces upto 3 digits = 9*1 + 90*2 + 900*3
    def findNthDigit(self, n: int) -> int:
        if n<=9: return n
        num = 9
        while n>= num*len(str(num)): # spaces upto
            n-=num*len(str(num))
            num*=10
        num = num//10
        res = int('9'*len(str(num))) # numbers upto len(str(num)) digits
        offset = n / (len(str(num)) + 1)
        offset = math.ceil(offset)
        res += offset
        idx = n % (len(str(num))+1)
        idx-=1
        res = str(res)
        return int(res[idx])

class MyTestCase(unittest.TestCase):
    def test1(self):
        n=3
        Output = 3
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test2(self):
        n=11
        Output = 0
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test3(self):
        n=12
        Output = 1
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test4(self):
        n=190
        Output = 1
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test5(self):
        n=191
        Output = 0
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test6(self):
        n=192
        Output = 0
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test7(self):
        n=193
        Output = 1
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test8(self):
        n=194
        Output = 0
        self.assertEqual(Output, get_sol().findNthDigit(n))
    def test9(self):
        n=195
        Output = 1
        self.assertEqual(Output, get_sol().findNthDigit(n))

import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/discuss/526301/Pigeon-hole
    # suppose that N > 2047 (2**11) then S must contains substrings of length 11
    # that represents all 1024 numbers from 1024 to 2047(all 11 bit numbers).
    # But it is not possible because S is 1000 long so it can have at most 990
    # substrings of length 11(total no of windows with window_size=11).
    # So we just need to check if N <= 2047.
    def queryString(self, s: str, n: int) -> bool:
        def get_no_of_bits(n):
            return len(bin(n)[2:])
        window_size = get_no_of_bits(n)
        left=2**(window_size-1)
        str_len=len(s)
        if (str_len - window_size + 1)<(n - left +1):
            return False
        for i in range(n , 0, -1):
            if bin(i)[2:] not in s: return False
        return True
class Solution2:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n , 0, -1):
            if bin(i)[2:] not in s: return False
        return True

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "0110"; n = 3
        Output= True
        self.assertEqual(Output,get_sol().queryString(s,n))
    def test_2(self):
        s = "0110"; n = 4
        Output= False
        self.assertEqual(Output,get_sol().queryString(s,n))
    def test_3(self):
        s = "1111000101"; n = 5
        Output= True
        self.assertEqual(Output,get_sol().queryString(s,n))
    def test_4(self):
        s = "10010111100001110010"; n = 10
        Output= False
        self.assertEqual(Output,get_sol().queryString(s,n))
    # def test_5(self):
    # def test_6(self):

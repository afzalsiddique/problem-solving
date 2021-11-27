import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def maskPII(self, s: str) -> str:
        def is_email(s):
            return '@' in s
        def mask_email(s:str):
            s = s.lower()
            name, domain = s.split('@')
            name = name[0] + '*'*5 + name[-1]
            return name + '@' + domain
        def remove_sep_char(s:str):
            sep = {'+', '-', '(', ')', ' '}
            return ''.join(x for x in s if x not in sep)
        def mask_number(s:str):
            s = remove_sep_char(s)
            s = s[::-1] # reverse
            res = s[:4] + '-***-***'
            if len(s)==10: return res[::-1]
            res += '-' + '*'*(len(s)-10) + '+'
            return res[::-1]

        return mask_email(s) if is_email(s) else mask_number(s)


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "LeetCode@LeetCode.com"
        Output= "l*****e@leetcode.com"
        self.assertEqual(Output, get_sol().maskPII(s))
    def test2(self):
        s = "AB@qq.com"
        Output= "a*****b@qq.com"
        self.assertEqual(Output, get_sol().maskPII(s))
    def test3(self):
        s = "1(234)567-890"
        Output= "***-***-7890"
        self.assertEqual(Output, get_sol().maskPII(s))
    def test4(self):
        s = "86-(10)12345678"
        Output= "+**-***-***-5678"
        self.assertEqual(Output, get_sol().maskPII(s))
    # def test5(self):
    # def test6(self):
    # def test7(self):

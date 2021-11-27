import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        total=len(encodedText)
        cols=total//rows
        res=[]
        for diff in range(cols):
            for i in range(rows):
                j=i+diff
                if j>=cols: break
                idx=i*cols+j
                res.append(encodedText[idx])
        while res and res[-1]==' ': res.pop() # remove spaces at the end
        return ''.join(res)




class MyTestCase(unittest.TestCase):
    def test1(self):
        encodedText,rows = "ch   ie   pr",  3
        Output= "cipher"
        self.assertEqual(Output, get_sol().decodeCiphertext(encodedText,rows))
    def test2(self):
        encodedText,rows = "iveo    eed   l te   olc",  4
        Output= "i love leetcode"
        self.assertEqual(Output, get_sol().decodeCiphertext(encodedText,rows))
    def test3(self):
        encodedText,rows = "coding",  1
        Output= "coding"
        self.assertEqual(Output, get_sol().decodeCiphertext(encodedText,rows))
    def test4(self):
        encodedText,rows = " b  ac",  2
        Output= " abc"
        self.assertEqual(Output, get_sol().decodeCiphertext(encodedText,rows))
    # def test5(self):
    # def test6(self):

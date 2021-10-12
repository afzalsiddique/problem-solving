import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def get_gcd(a,b):
            if b>a: return get_gcd(b,a)
            if a%b==0: return b
            return get_gcd(b, a%b)

        count = Counter()
        res = 0
        for width,height in rectangles:
            gcd = get_gcd(width,height)
            w = width//gcd # convert to simplest form
            h = height//gcd
            if (w,h) in count:
                res+=count[w,h]
            count[w,h]+=1
        return res
class Solution2:
    # bad solution. precision of floating number is lost
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = Counter()
        res = 0
        for w,h in rectangles:
            if w/h in count:
                res+=count[w/h]
            count[w/h]+=1
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        rectangles = [[4,8],[3,6],[10,20],[15,30]]
        Output= 6
        self.assertEqual(Output, get_sol().interchangeableRectangles(rectangles))
    def test2(self):
        rectangles = [[4,5],[7,8]]
        Output= 0
        self.assertEqual(Output, get_sol().interchangeableRectangles(rectangles))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)<k:
            return [s+fill*(max(0,k-len(s)))]
        res=[]
        for i in range(0,len(s),k):
            res.append(s[i:i+k])
        if len(res[-1])<k:
            res[-1]=s[i:]+fill*(k-len(res[-1]))
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(["abc","def","ghi"],get_sol().divideString(s = "abcdefghi", k = 3, fill = "x"))
    def test2(self):
        self.assertEqual(["abc","def","ghi","jxx"],get_sol().divideString(s = "abcdefghij", k = 3, fill = "x"))
    def test3(self):
        self.assertEqual(["ctoyjrwt","ngqwtnnn"],get_sol().divideString("ctoyjrwtngqwt", 8, "n"))
    def test4(self):
        self.assertEqual(["bgycymgbblobvpdfuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"],get_sol().divideString("bgycymgbblobvpdf", 67, "u"))
    # def test5(self):

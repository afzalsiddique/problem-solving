import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def longestDecomposition(self, text: str) -> int:
        def recur(s:str):
            if not s: return 0
            for i in range(1,len(s)):
                first=s[:i]
                last=s[-i:]
                if first==last:
                    return 2+recur(s[i:-i])
            return 1

        return recur(text)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(7,get_sol().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
    def test02(self):
        self.assertEqual(1,get_sol().longestDecomposition("merchant"))
    def test03(self):
        self.assertEqual(11,get_sol().longestDecomposition("antaprezatepzapreanta"))
    def test04(self):
        self.assertEqual(3,get_sol().longestDecomposition("helloadamhello"))
    def test05(self):
        self.assertEqual(2,get_sol().longestDecomposition("abcabc"))
    # def test06(self):

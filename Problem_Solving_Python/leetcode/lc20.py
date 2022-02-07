from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        di = {'{':'}','[':']','(':')'}
        for c in s:
            if c not in di: # if closing
                if not st:return False # closing coming before opening
                if di[st[-1]] != c:return False # closing coming with corresponding opening
                st.pop()
            else: # if opening
                st.append(c)
        if st:
            return False
        return True

class MyTestClass(unittest.TestCase):
    def test_1(self):
        actual = get_sol().isValid("()")
        expected = True
        self.assertEqual(expected, actual)
    def test_2(self):
        actual = get_sol().isValid("()[]{}")
        expected = True
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = get_sol().isValid("(]")
        expected = False
        self.assertEqual(expected, actual)
    def test_4(self):
        actual = get_sol().isValid("([)]")
        expected = False
        self.assertEqual(expected, actual)
    def test_5(self):
        actual = get_sol().isValid("]")
        expected = False
        self.assertEqual(expected, actual)

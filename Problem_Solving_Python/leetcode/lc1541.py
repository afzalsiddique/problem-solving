import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minInsertions(self, s: str) -> int:
        st_size=0 # size of the stack.
        cnt=0
        for ch in s:
            if ch == '(':
                if st_size%2:
                    st_size-=1
                    cnt+=1
                st_size+=2
            else:
                if not st_size:
                    st_size+=2
                    cnt+=1
                st_size-=1
        return st_size+cnt
class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "(()))"
        Output= 1
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_2(self):
        s = "())"
        Output= 0
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_3(self):
        s = "))())("
        Output= 3
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_4(self):
        s = "(((((("
        Output= 12
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_5(self):
        s = ")))))))"
        Output= 5
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_6(self):
        s = ")"
        Output= 2
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_7(self):
        s = "))"
        Output= 1
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_8(self):
        s = "))))"
        Output= 2
        self.assertEqual(Output, get_sol().minInsertions(s))
    def test_9(self):
        s = "(()))(()))()())))"
        Output= 4
        self.assertEqual(Output, get_sol().minInsertions(s))

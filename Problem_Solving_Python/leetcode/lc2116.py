import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        li=list(s)
        locked=[x=='1' for x in locked]
        cnt=0
        q=deque()
        for i in range(len(li)):
            c=li[i]
            if c=='(':
                cnt+=1
            else:
                cnt-=1
                if not locked[i]:
                    q.append(i)
            if cnt==-1:
                if q:
                    idx=q.popleft()
                    li[i]=idx
                    cnt=1
                else:
                    return False

        cnt=0
        q=deque()
        for i in range(len(li)-1,-1,-1):
            c=li[i]
            if c==')':
                cnt+=1
            else:
                cnt-=1
                if not locked[i]:
                    q.append(i)
            if cnt==-1:
                if q:
                    idx=q.popleft()
                    li[i]=idx
                    cnt=1
                else:
                    return False
        if not cnt: return True
        return False


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().canBeValid( s = "))()))", locked = "010100"))
    def test2(self):
        self.assertEqual(True, get_sol().canBeValid(s = "()()", locked = "0000"))
    def test3(self):
        self.assertEqual(False, get_sol().canBeValid(s = ")", locked = "0"))
    def test4(self):
        self.assertEqual(True, get_sol().canBeValid(s = "(()(", locked = "1110"))
    def test5(self):
        self.assertEqual(False, get_sol().canBeValid(s = "(()(", locked = "1111"))
    def test6(self):
        self.assertEqual(False, get_sol().canBeValid(")())", "1110"))
    def test7(self):
        self.assertEqual(True, get_sol().canBeValid("())())", "101110"))
    def test8(self):
        self.assertEqual(True, get_sol().canBeValid("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))
    def test9(self):
        self.assertEqual(True, get_sol().canBeValid("()()()))))", "1010111111"))

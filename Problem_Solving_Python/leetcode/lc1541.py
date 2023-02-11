import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minInsertions(self, s: str) -> int:
        remainingClosing=0 # no of closing parenthesis left to balance off
        insert=0 # total insertion
        for ch in s:
            if ch == '(':
                if remainingClosing%2: # out of 2 two closing parenthesis, 1 has been balanced off.
                    remainingClosing-=1 # balance off by inserting closing parenthesis
                    insert+=1 # insert closing parenthesis
                remainingClosing+=2
            else:
                if not remainingClosing:
                    insert+=1 # insert opening parenthesis
                    remainingClosing+=2
                remainingClosing-=1
        return remainingClosing+insert
class Solution2:
    def minInsertions(self, s: str) -> int:
        def isTwoClosing(i):
            if i+1==n: return False
            return s[i]==s[i+1]==')'

        n=len(s)
        left,insert = 0,0
        i=0
        while i<n:
            if s[i]=='(':
                left+=2
            else:
                if left:
                    left-=2
                    if isTwoClosing(i):
                        i+=1 # two closing found. move one more step to the right
                    else: # one closing
                        insert+=1 # another closing required
                else: # not enough opening
                    if isTwoClosing(i):
                        insert+=1 # one opening required
                        i+=1 # two closing found. move one more step to the right
                    else:
                        insert+=2 # one opening and one closing required
            i+=1
        return insert+left
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().minInsertions("(()))"))
    def test02(self):
        self.assertEqual(0, get_sol().minInsertions("())"))
    def test03(self):
        self.assertEqual(3, get_sol().minInsertions("))())("))
    def test04(self):
        self.assertEqual(12, get_sol().minInsertions("(((((("))
    def test05(self):
        self.assertEqual(5, get_sol().minInsertions(")))))))"))
    def test06(self):
        self.assertEqual(2, get_sol().minInsertions(")"))
    def test07(self):
        self.assertEqual(1, get_sol().minInsertions("))"))
    def test08(self):
        self.assertEqual(2, get_sol().minInsertions("))))"))
    def test09(self):
        self.assertEqual(4, get_sol().minInsertions("(()))(()))()())))"))
    def test10(self):
        self.assertEqual(2, get_sol().minInsertions("()))"))
    def test11(self):
        self.assertEqual(1, get_sol().minInsertions("(()))"))
    def test12(self):
        self.assertEqual(3, get_sol().minInsertions("()()))"))

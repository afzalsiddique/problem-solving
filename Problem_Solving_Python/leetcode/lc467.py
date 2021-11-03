import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP
    def findSubstringInWraproundString(self, p: str) -> int:
        def prev_char(c,step=1):
            tmp = ord(c)-ord('a')-step
            tmp%=26
            tmp+=ord('a')
            return chr(tmp)
        di = {c:0 for c in string.ascii_lowercase} # max length of substring ending at this char

        cnt = 0
        for i in range(len(p)):
            if i>0 and prev_char(p[i])==p[i-1]:
                cnt+=1
            else:
                cnt=1
            di[p[i]]=max(di[p[i]], cnt)

        res = 0
        for c in di:
            res+=di[c]
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        p = "a"
        Output= 1
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test2(self):
        p = "cac"
        Output= 2
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test3(self):
        p = "zab"
        Output= 6
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test4(self):
        p = "zaba"
        Output= 6
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test5(self):
        p = "abaab"
        Output= 3
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test6(self):
        p = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        Output= 1703
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))
    def test7(self):
        p = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        Output= 33475
        self.assertEqual(Output, get_sol().findSubstringInWraproundString(p))

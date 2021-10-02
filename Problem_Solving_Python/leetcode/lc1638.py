import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/917701/C%2B%2BJavaPython3-O(n-3)-greater-O(n-2)
    def countSubstrings(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        res=0
        for i in range(m):
            for j in range(n):
                if s[i]!=t[j]:
                    l,r=1,1
                    while min(i-l,j-l)>=0  and s[i-l]==t[j-l]:
                        l+=1
                    while max(i+r,j+r)<min(m,n) and s[i+r]==t[j+r]:
                        r+=1
                    res += l*r
        return res
class Solution3:
    # https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/917701/C%2B%2BJavaPython3-O(n-3)-greater-O(n-2)
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                window = 0
                diff = 0
                while diff <= 1 and i + window < len(s) and j + window < len(t):
                    diff += s[i + window] != t[j + window]
                    if diff==1: res+=1
                    window += 1
        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "aba"
        t = "baba"
        Output = 6
        self.assertEqual(Output, get_sol().countSubstrings(s, t))

    def test_2(self):
        s = "ab"
        t = "bb"
        Output = 3
        self.assertEqual(Output, get_sol().countSubstrings(s, t))

    def test_3(self):
        s = "a"
        t = "a"
        Output = 0
        self.assertEqual(Output, get_sol().countSubstrings(s, t))

    def test_4(self):
        s = "abe"
        t = "bbc"
        Output = 10
        self.assertEqual(Output, get_sol().countSubstrings(s, t))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

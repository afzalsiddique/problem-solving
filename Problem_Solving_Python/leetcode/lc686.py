import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a: return 1
        if b in (a+a): return 2
        index = b.find(a)
        res=1
        if index !=0: # check left of 'index'
            j=index-1
            i=len(a)-1
            while j!=-1:
                if a[i]!=b[j]: return -1
                j-=1
                i-=1
            res+=1

        j = index+len(a)
        while j<len(b):
            i=0
            res+=1
            while i<len(a) and j<len(b):
                if a[i]!=b[j]: return -1
                i+=1
                j+=1
        return res
class Solution2:
    # https://leetcode.com/problems/repeated-string-match/discuss/108084/C%2B%2B-4-lines-O(m-*-n)-or-O(1)-and-KMP-O(m-%2B-n)-or-O(n)
    # tle. time O(m*n) space O(1)
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m,n=len(a),len(b)
        for idx in range(m):
            res=1
            i=idx
            j=0
            while j<n:
                if a[i]==b[j]:
                    j+=1
                    i+=1
                    if i==m:
                        res+=1
                        i=0
                else:
                    break
            if j==n:
                if i==0: res-=1 # ends at the last index of a
                return res
        return -1


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().repeatedStringMatch("abcd",  "cdabcdab"))
    def test02(self):
        self.assertEqual(2, get_sol().repeatedStringMatch("a",  "aa"))
    def test03(self):
        self.assertEqual(1, get_sol().repeatedStringMatch("a",  "a"))
    def test04(self):
        self.assertEqual(-1, get_sol().repeatedStringMatch("abc",  "wxyz"))
    def test05(self):
        self.assertEqual(1, get_sol().repeatedStringMatch("aa", "a"))
    def test06(self):
        self.assertEqual(2, get_sol().repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba"))
    def test07(self):
        self.assertEqual(-1, get_sol().repeatedStringMatch("cxabcd", "cdabcdab"))
    def test08(self):
        self.assertEqual(-1, get_sol().repeatedStringMatch("abcabcabcabc", "abac"))
    def test09(self):
        self.assertEqual(3, get_sol().repeatedStringMatch("baa", "abaab"))
    def test10(self):
        self.assertEqual(10, get_sol().repeatedStringMatch("baaabbbaba", "baaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbaba"))
    def test11(self):
        self.assertEqual(3, get_sol().repeatedStringMatch("baaabbbaba", "ababaaabbbababaaabbbaba"))
    def test12(self):
        self.assertEqual(3, get_sol().repeatedStringMatch("abc","bcabcabc"))

import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution2()
# z algo
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_z_values(s):
            n, l, r = len(s), 0, 0
            z = [0 for _ in range(n)]
            for i in range(1, n):
                if i > r:
                    l, r = i, i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
                else:
                    if z[i - l] + i - 1 < r:
                        z[i] = z[i - l]
                    else:
                        l = i
                        while r < n and s[r - l] == s[r]:
                            r += 1
                        z[i] = r - l
                        r -= 1
            return z

        m,n = len(needle), len(haystack)
        if m==0:return 0
        z = get_z_values(needle+"$"+haystack)
        for i in range(m+1, n+m+1):
            if z[i] == m:
                return i- m-1
        return -1

# KMP algo
class Solution2:
    # creating lps
    def computeLPSArray(self, pat): # geeksforgeeks
        j = 0 # length of the previous longest prefix suffix
        i = 1
        n = len(pat)
        lps=[0]*n
        while i < n:
            if pat[i]== pat[j]:
                lps[i] = j+1
                i += 1
                j += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1] # go back to previous longest prefix suffix
        return lps
    # finding pattern
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.computeLPSArray(needle)
        m,n=len(haystack),len(needle)
        if n==0: return 0
        j=0
        i=0
        while i<m:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==len(needle):
                    return i-n
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
        return -1
    def computeLPSArray2(self,pat:str): # abdul bari version
        pat = '#' + pat
        n = len(pat)
        i=2
        j=0
        lps=[0]*n
        while i<n:
            if pat[i]==pat[j+1]:
                lps[i]=j+1
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j]
        return lps[1:]

    # finding pattern
    def strStr2(self, haystack: str, needle: str) -> int:
        m,n= len(haystack), len(needle)
        if n==0:return 0
        if m==0:return -1
        i,j=0,0
        lps = self.computeLPSArray(needle)
        while i<m:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==n:
                return i-j
            elif i<m and needle[j]!=haystack[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1

class Solution3:
    # brute force
    def strStr(self, haystack: str, needle: str) -> int:
        m,n=len(haystack),len(needle)

        if n==0:return 0
        if m==0:return -1

        for i in range(m):
            if i+n>m:break
            for j in range(n):
                if haystack[i+j]!=needle[j]:
                    break
                if j == n-1:
                    return i
        return -1



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().strStr("hello", "ll"))
    def test02(self):
        self.assertEqual(-1, get_sol().strStr("aaaaa", "bba"))
    def test03(self):
        self.assertEqual(0, get_sol().strStr("", ""))
    def test04(self):
        self.assertEqual(0, get_sol().strStr("a","a"))
    def test05(self):
        self.assertEqual(0, get_sol().strStr("mississippi","mississippi"))
    def test06(self):
        self.assertEqual(-1, get_sol().strStr( "mississippi" ,"issipi"))
    def test07(self):
        self.assertEqual(4, get_sol().strStr( "mississippi" ,"issip"))
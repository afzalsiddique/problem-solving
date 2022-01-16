import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # tle
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def getLi(s:str):
            n=len(s)
            i=0
            li=[]
            while i<n:
                j=i
                while j<n and s[j]==s[i]:
                    j+=1
                li.append((s[i],j-i))
                i=j
            return li
        def getS(li):
            return ''.join([c*freq for c,freq in li])
        @functools.lru_cache(None)
        def getEncodingLength(s:str):
            n=len(s)
            i=0
            res=0
            while i<n:
                j=i
                while j<n and s[j]==s[i]:
                    j+=1
                if j-i>1:
                    res+=1+len(str(j-i))
                else:
                    res+=1
                i=j
            return res
        @functools.lru_cache(None)
        def f(s:str,k:int):
            if k==0:
                return getEncodingLength(s)
            if k<0:
                return float('inf')
            res=float('inf')
            res=min(res,getEncodingLength(s))
            li=getLi(s)
            for i,(c,freq) in enumerate(li):
                newLi=li[:i]+[[c,li[i][1]-1]]+li[i+1:]
                newLi2=li[:i]+li[i+1:]
                newLi3=li[:i]+[[c,1]]+li[i+1:]
                res=min(res,f(getS(newLi),k-1))
                res=min(res,f(getS(newLi2),k-freq))
                if freq>1 and freq<=k:
                    res=min(res,f(getS(newLi3),k-(freq-1)))
            return res

        return f(s,k)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().getLengthOfOptimalCompression("aaabcccd",2))
    def test02(self):
        self.assertEqual(2, get_sol().getLengthOfOptimalCompression("aabbaa", 2))
    def test03(self):
        self.assertEqual(3, get_sol().getLengthOfOptimalCompression("aaaaaaaaaaa", 0))
    def test04(self):
        self.assertEqual(1, get_sol().getLengthOfOptimalCompression("abc", 2))
    def test05(self):
        self.assertEqual(4, get_sol().getLengthOfOptimalCompression("llllllllllttttttttt", 1))
    def test06(self):
        self.assertEqual(4, get_sol().getLengthOfOptimalCompression("abcdefghijklmnopqrstuvwxyz", 16))


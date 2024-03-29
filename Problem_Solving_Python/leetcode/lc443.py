import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def compress(self, chars: List[str]) -> int:
        INVALID='-'
        n=len(chars)
        prev=INVALID
        cnt=0
        idx=0
        for i in range(n+1): # one extra iteration to deal with the last char
            c=INVALID if i==n else chars[i]
            if c!=prev:
                if cnt!=0:
                    chars[idx]=prev
                    idx+=1
                    if cnt>1:
                        s=str(cnt)
                        for j in range(len(s)):
                            chars[idx]=s[j]
                            idx+=1
                cnt=0
            cnt+=1
            prev=c
        return idx
class Solution2:
    def compress(self, chars: List[str]) -> int:
        def place_number(ch, count):
            nonlocal pos
            chars[pos] = ch
            pos+=1
            if count==1: return
            count = str(count)
            i=0
            while i<len(count):
                chars[pos] = count[i]
                pos+=1
                i+=1

        n=len(chars)
        left,right = 0,0
        pos=0 # char will be placed at this position
        while right<n:
            while right<n and chars[left]==chars[right]:
                right+=1
            cnt = right-left
            place_number(chars[left], cnt)
            left = right
        return pos



class MyTestCase(unittest.TestCase):
    def test01(self):
        chars = ["a","a","b","b","c","c","c"]
        expected1, expected2 = 6, ["a","2","b","2","c","3"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test02(self):
        chars = ["a"]
        expected1, expected2 = 1, ["a"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test03(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected1, expected2 = 4, ["a","b","1","2"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test04(self):
        chars = ["a","a","a","b","b","a","a"]
        expected1, expected2 = 6, ["a","3","b","2","a","2"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test05(self):
        chars = ["a","a","a","a","a","b"]
        expected1, expected2 = 3, ["a","5","b"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test06(self):
        chars = ["a","a","b","b","c","c","c"]
        expected1, expected2 = 6, ["a","2","b","2","c","3"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)
    def test07(self):
        chars = ["#","$","#","#","$","$","$","$","#","#"]
        expected1, expected2 = 8, ["#","$","#","2","$","4","#","2"]
        Output1 = get_sol().compress(chars)
        self.assertEqual(expected2, chars[:expected1])
        self.assertEqual(expected1, Output1)


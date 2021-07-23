import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/decoded-string-at-index/discuss/979066/Python-O(n)-solution-explained
    # https://www.youtube.com/watch?v=6iE7QJRMXzs
    def decodeAtIndex(self, s, k):
        lengths=[]
        for i in range(len(s)):
            if not lengths:
                lengths.append(1)
            elif s[i].isdigit():
                lengths.append(lengths[-1]*int(s[i]))
            else:
                lengths.append(lengths[-1]+1)
        # print(lengths)
        i=len(s)
        while i>0:
            k%=lengths[i-1]
            if k==0 and not s[i-1].isdigit():
                return s[i-1]
            i-=1
class Solution2:
    # tle
    def decodeAtIndex(self, s: str, left: int) -> str:
        res=[]
        i=0
        while left and i<len(s):
            if '2'<=s[i]<='9':
                j=0
                tmp=len(res)
                while left and j<int(s[i])-1:
                    k=0
                    while left and k<tmp:
                        res.append(res[k])
                        left-=1
                        k+=1
                    j+=1
            else:
                res.append(s[i])
                left-=1
            i+=1
        return res[-1]


class tester(unittest.TestCase):
    def test_1(self):
        s = "leet2code3"
        l = 10
        Output= "o"
        self.assertEqual(Output,get_sol().decodeAtIndex(s,l))
    def test_2(self):
        s = "ha22"
        l = 5
        Output= "h"
        self.assertEqual(Output,get_sol().decodeAtIndex(s,l))
    def test_3(self):
        s = "a2345678999999999999999"
        l = 1
        Output= "a"
        self.assertEqual(Output,get_sol().decodeAtIndex(s,l))
    def test_4(self):
        s = "y959q969u3hb22odq595"
        l = 222280369
        Output= "unknown"
        self.assertEqual(Output,get_sol().decodeAtIndex(s,l))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
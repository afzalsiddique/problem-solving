import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        if len(s)==1:
            return N
        flag=True
        i=0
        while i+1<len(s):
            if s[i]>s[i+1]:
                flag=False
                break
            i+=1
        if flag:
            return N
        while i-1>=0:
            if s[i]==s[i-1]:
                i-=1
            else:
                break
        res=[]
        res.append(s[:i])
        res.append(str(int(s[i])-1))
        res.append('9'*(len(s)-i-1))
        return int(''.join(res))

class tester(unittest.TestCase):
    def test_1(self):
        n = 10
        Output= 9
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_2(self):
        n = 1234
        Output= 1234
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_3(self):
        n = 332
        Output= 299
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_4(self):
        n=0
        Output=0
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_5(self):
        n=120
        Output=119
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_7(self):
        n=11013
        Output= 9999
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_8(self):
        n=35552
        Output=34999
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))
    def test_9(self):
        n=35582
        Output=35579
        self.assertEqual(Output,get_sol().monotoneIncreasingDigits(n))

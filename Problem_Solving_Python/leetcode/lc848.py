import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        cur=0
        s=[ord(c)-ord('a') for c in s]
        for i in reversed(range(len(s))):
            cur+=shifts[i]
            s[i]+=cur
            s[i]%=26
        s=list(map(lambda c:chr(c+ord('a')),s))
        return ''.join(s)
class Solution2:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        cum_sum=list(itertools.accumulate(shifts,operator.add))
        cum_sum.reverse()
        # print(cum_sum)
        s=[ord(c)-ord('a') for c in s]
        for i in range(len(cum_sum)):
            s[i]+=cum_sum[i]
            s[i]%=26
        s=list(map(lambda c:chr(c+ord('a')),s))
        return ''.join(s)

class tester(unittest.TestCase):
    def test_1(self):
        s = "abc"
        shifts = [3,5,9]
        Output= "rpl"
        self.assertEqual(Output,get_sol().shiftingLetters(s,shifts))
    # def test_2(self):
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):

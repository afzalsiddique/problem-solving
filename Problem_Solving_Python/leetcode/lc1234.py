import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def balancedString(self, s: str) -> int:
        def valid(): return all(di[ch]>=count[ch] for ch in 'QWER')
        n=len(s)
        count = Counter(s)
        for ch in count:
            count[ch]-=n//4
        di= Counter()
        left=right=0
        minn=float('inf')
        while right<n:
            while right<n and not valid(): # if not enough chars inside window add right char to the window
                di[s[right]]+=1
                right+=1
            while left<n and valid(): # if enough chars inside window remove left char from the window
                minn=min(minn,right-left)
                di[s[left]]-=1
                left+=1
        return minn

class tester(unittest.TestCase):
    def test_1(self):
        s = "QWER"
        Output= 0
        self.assertEqual(Output,get_sol().balancedString(s))
    def test_2(self):
        s = "QQWE"
        Output= 1
        self.assertEqual(Output,get_sol().balancedString(s))
    def test_3(self):
        s = "QQQW"
        Output= 2
        self.assertEqual(Output,get_sol().balancedString(s))
    def test_4(self):
        s = "QQQQ"
        Output= 3
        self.assertEqual(Output,get_sol().balancedString(s))
    def test_5(self):
        s = "WWEQERQWQWWRWWERQWEQ"
        Output= 4
        self.assertEqual(Output,get_sol().balancedString(s))
    def test_6(self):
        s = "WQWRQQQW"
        Output= 3
        self.assertEqual(Output,get_sol().balancedString(s))
    # def test_7(self):
    # def test_8(self):

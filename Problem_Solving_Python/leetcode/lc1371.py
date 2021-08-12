import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=ReZpa5vxRKc
# https://www.youtube.com/watch?v=yuewgcX6PlY
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        di={0:-1}
        vowels={'a':0,'e':1,'i':2,'o':3,'u':4}
        mask=0
        maxx=0
        for i,ch in enumerate(s):
            if ch in vowels:
                idx=vowels[ch]
                mask=mask ^ (1<<idx) # flip

            # xor is similar to adding even and odds. even+even=even ie 0^0=0. even+odd=odd ie 0^1=1. odd+even=odd. 1^0=1. odd+odd=even ie 1^1=0
            if int('00000',2)^mask in di: # equivalent to target-running_sum. target='00000' means even 'a's, even 'e's etc
                maxx=max(maxx,i-di[mask])

            if mask not in di:
                di[mask]=i
        return maxx
class Solution2:
    def findTheLongestSubstring(self, s: str) -> int:
        di={0:-1}
        vowels={'a':0,'e':1,'i':2,'o':3,'u':4}
        mask=0
        maxx=0
        for i,ch in enumerate(s):
            if ch in vowels:
                idx=vowels[ch]
                mask=mask ^ (1<<idx) # flip
            if mask in di:
                maxx=max(maxx,i-di[mask])
            else:
                di[mask]=i
        return maxx
class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "eleetminicoworoep"
        Output= 13
        self.assertEqual(Output, get_sol().findTheLongestSubstring(s))
    def test_2(self):
        s = "leetcodeisgreat"
        Output= 5
        self.assertEqual(Output, get_sol().findTheLongestSubstring(s))
    def test_3(self):
        s = "bcbcbc"
        Output= 6
        self.assertEqual(Output, get_sol().findTheLongestSubstring(s))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
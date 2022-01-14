import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def rotatedDigits(self, n: int) -> int:
        SAME,GOOD,INVALID=0,1,2
        sameSet,goodSet,invalidSet={0,1,8},{2,5,6,9},{3,4,7}
        res=0
        dp=[-99]*(n+1)
        for i in range(min(n,9)+1):
            if i in sameSet:
                dp[i]=SAME
            elif i in goodSet:
                dp[i]=GOOD
                res+=1
            else:
                dp[i]=INVALID

        for i in range(10,n+1):
            lastDigits=dp[i//10]
            thisDigit=dp[i%10]
            if lastDigits==INVALID or thisDigit==INVALID:
                dp[i]=INVALID
            elif lastDigits==SAME and thisDigit==SAME:
                dp[i]=SAME
            else:
                dp[i]=GOOD
                res+=1
        return res
class Solution2:
    def rotatedDigits(self, n: int) -> int:
        SAME,GOOD,INVALID=0,1,2
        sameSet,goodSet,invalidSet={0,1,8},{2,5,6,9},{3,4,7}
        res=0
        dp=[-99]*(n+1)
        for i in range(min(n,9)+1):
            if i in sameSet:
                dp[i]=SAME
            elif i in goodSet:
                dp[i]=GOOD
                res+=1
            else:
                dp[i]=INVALID

        for i in range(10,n+1):
            lastDigits=dp[i//10]
            thisDigit=dp[i%10]
            if lastDigits==INVALID or thisDigit==INVALID:
                dp[i]=INVALID
            elif lastDigits==SAME:
                if thisDigit==SAME:
                    dp[i]=SAME
                elif thisDigit==GOOD:
                    dp[i]=GOOD
                    res+=1
            elif lastDigits==GOOD:
                if thisDigit==SAME:
                    dp[i]=GOOD
                    res+=1
                elif thisDigit==GOOD:
                    dp[i]=GOOD
                    res+=1
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().rotatedDigits(10))
    def test02(self):
        self.assertEqual(0,get_sol().rotatedDigits(1))
    def test03(self):
        self.assertEqual(1,get_sol().rotatedDigits(2))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):

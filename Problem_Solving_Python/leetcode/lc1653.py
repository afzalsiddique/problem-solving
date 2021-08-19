from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bcount = 0
        for l in s:
            if l == 'a':
                # either remove this 'a': res + 1
                # or keep this 'a': bcount (must remove all previous 'b's)
                res = min(res + 1, bcount)
            else:
                # Fine for 'b' in the tail
                bcount += 1
        return res
class Solution2:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        after_a=[0]*n
        before_b=[0]*n

        cnt=0
        for i in range(n):
            if s[i]=='b':
                cnt+=1
            before_b[i]=cnt

        cnt=0
        for i in reversed(range(n)):
            if s[i]=='a':
                cnt+=1
            after_a[i]=cnt

        ans=float('inf')
        for i in range(n):
            ans=min(ans,after_a[i]+before_b[i])
        return ans-1

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "aababbab"
        Output= 2
        self.assertEqual(Output, get_sol().minimumDeletions(s))
    def test_2(self):
        s = "bbaaaaabb"
        Output= 2
        self.assertEqual(Output, get_sol().minimumDeletions(s))
    def test_3(self):
        s = "aaaaaaaaaaaaaa"
        Output= 0
        self.assertEqual(Output, get_sol().minimumDeletions(s))
    def test_4(self):
        s = "bbbbbbbbbb"
        Output= 0
        self.assertEqual(Output, get_sol().minimumDeletions(s))
    def test_5(self):
        s = "aaaaaabbbbabaaaabbabaaabbabbbaaabababaaaaaaabbaaabaaababaaabababa"
        Output= 24
        self.assertEqual(Output, get_sol().minimumDeletions(s))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
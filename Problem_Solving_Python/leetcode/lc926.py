import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minFlipsMonoIncr(self, s):
        n = len(s)
        cnt0=0
        cnt1 = 0
        for i in range(n):
            if s[i]=='0':
                cnt0+=1
        res = n - cnt0
        for i in range(n):
            if s[i] == '0':
                cnt0 -= 1
            elif s[i] == '1':
                res = min(res, cnt1+cnt0)
                cnt1 += 1
        return res
class Solution2:
    # https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183851/C%2B%2BJava-4-lines-O(n)-or-O(1)-DP
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        one_before=[0 for _ in range(n)]
        zero_after=[0 for _ in range(n)]
        cnt=0
        for i in range(n):
            if s[i]=='1':
                cnt+=1
            one_before[i]=cnt

        cnt=0
        for i in reversed(range(n)):
            if s[i]=='0':
                cnt+=1
            zero_after[i]=cnt
        # print(one_before)
        # print(zero_after)
        minn=float('inf')
        for i in range(0,n):
            minn=min(minn,one_before[i]+zero_after[i])
        return minn-1
class Solution3:
    # https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183851/C%2B%2BJava-4-lines-O(n)-or-O(1)-DP
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        one_before=[0 for _ in range(n)]
        zero_after=[0 for _ in range(n)]
        cnt=0
        for i in range(n):
            if s[i]=='1':
                cnt+=1
            one_before[i]=cnt
        one_before=[0] + one_before + [one_before[-1]]

        cnt=0
        for i in reversed(range(n)):
            if s[i]=='0':
                cnt+=1
            zero_after[i]=cnt
        zero_after = [zero_after[-1]] + zero_after + [0]

        # print(one_before)
        # print(zero_after)
        minn=float('inf')
        for i in range(0,n+1):
            minn=min(minn,one_before[i]+zero_after[i+1])
        return minn

class tester(unittest.TestCase):
    def test_1(self):
        s = "00110"
        Output= 1
        self.assertEqual(Output, get_sol().minFlipsMonoIncr(s))
    def test_2(self):
        s = "010110"
        Output= 2
        self.assertEqual(Output, get_sol().minFlipsMonoIncr(s))
    def test_3(self):
        s = "00011000"
        Output= 2
        self.assertEqual(Output, get_sol().minFlipsMonoIncr(s))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
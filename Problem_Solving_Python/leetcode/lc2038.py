import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq=defaultdict(int)
        cnt=0
        last='#'
        for c in colors:
            if c!=last:
                freq[last]+=max(0,cnt-2)
                cnt=1
                last=c
            else:
                cnt+=1
        freq[last] += max(0, cnt - 2)
        return freq['A']>freq['B']
class Solution3:
    def winnerOfGame(self, colors: str) -> bool:
        alice,bob=0,0
        cnt=0
        last='#'
        for c in colors:
            if c!=last:
                if last=='A':
                    alice+=max(0,cnt-2)
                elif last=='B':
                    bob+=max(0,cnt-2)
                cnt=1
                last=c
            else:
                cnt+=1
        if last=='A':
            alice+=max(0,cnt-2)
        elif last=='B':
            bob+=max(0,cnt-2)
        return alice>bob

class Solution2:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        i=0
        a_counts = []
        b_counts = []
        while i<n:
            cnt_a,cnt_b=0,0
            while i<n and colors[i]=='A':
                cnt_a+=1
                i+=1
            while i<n and colors[i]=='B':
                cnt_b+=1
                i+=1
            a_counts.append(cnt_a)
            b_counts.append(cnt_b)
        a_ans,b_ans=0,0
        for a in a_counts:
            if a>=3:
                a_ans+=a-2
        for b in b_counts:
            if b>=3:
                b_ans+=b-2
        # print(a_ans,b_ans)
        return a_ans>b_ans


class MyTestCase(unittest.TestCase):
    def test1(self):
        colors = "AAABABB"
        Output= True
        self.assertEqual(Output, get_sol().winnerOfGame(colors))
    def test2(self):
        colors = "AA"
        Output= False
        self.assertEqual(Output, get_sol().winnerOfGame(colors))
    def test3(self):
        colors = "ABBBBBBBAAA"
        Output= False
        self.assertEqual(Output, get_sol().winnerOfGame(colors))
    def test4(self):
        colors = "BBBAAAABB"
        Output= True
        self.assertEqual(Output, get_sol().winnerOfGame(colors))
    def test5(self):
        colors = "AAAABBBB"
        Output= False
        self.assertEqual(Output, get_sol().winnerOfGame(colors))
    # def test6(self):



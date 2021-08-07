import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n=len(text)
        count=Counter(text)
        begin,end=0,0
        li=[]
        while end<n:
            while end<n and text[begin]==text[end]:
                end+=1
            li.append((text[begin],end-begin))
            begin=end

        m=len(li)
        maxx=max(li[i][1] for i in range(m))
        for i in range(1,m-1):
            cur_c,cur_freq=li[i]
            prev_c,prev_freq=li[i-1]
            nxt_c,nxt_freq=li[i+1]
            if cur_freq==1 and prev_c==nxt_c:
                if prev_freq+nxt_freq<count[prev_c]:
                    maxx=max(maxx,prev_freq+nxt_freq+1)
                else:
                    maxx=max(maxx,prev_freq+nxt_freq)
            else:
                if prev_freq<count[prev_c]:
                    maxx=max(maxx,prev_freq+1)
                if nxt_freq<count[nxt_c]:
                    maxx=max(maxx,nxt_freq+1)
        return maxx


class Tester(unittest.TestCase):
    def test_1(self):
        text = "ababa"
        Output= 3
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    def test_2(self):
        text = "aaabaaa"
        Output= 6
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    def test_3(self):
        text = "aaabbaaa"
        Output= 4
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    def test_4(self):
        text = "aaaaa"
        Output= 5
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    def test_5(self):
        text = "abcdef"
        Output= 1
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    def test_6(self):
        text = "aaabaaacca"
        Output= 7
        self.assertEqual(Output,get_sol().maxRepOpt1(text))
    # def test_7(self):
    # def test_8(self):

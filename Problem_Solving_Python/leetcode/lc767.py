from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # 1. Count the frequency
    # 2. Find the most frequent char and its frequency
    # 3. Check if the most frequent char occurs more than half of ceiling value
    # 4. Place the most frequent char in even spaces
    # 5. Place chars in remaining even spaces
    # 6. Place chars in odd spaces
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        freq=[0]*26
        most_freq_char='#'
        most_freq=0
        for c in s:
            idx=ord(c)-ord('a')
            freq[idx]+=1
            if freq[idx]>most_freq:
                most_freq=freq[idx]
                most_freq_char=c


        if any(freq[i]>(n+1)//2 for i in range(26)): return ""

        freq[ord(most_freq_char)-ord('a')]=0
        res=['']*n

        i=0
        while most_freq:
            res[i]=most_freq_char
            most_freq-=1
            i+=2

        pos=0
        while i<n:
            while i<n and freq[pos]:
                res[i]=chr(pos+ord('a'))
                freq[pos]-=1
                i+=2
            pos+=1

        pos=0
        i=1
        while i<n:
            while i<n and freq[pos]:
                res[i]=chr(pos+ord('a'))
                freq[pos]-=1
                i+=2
            pos+=1
        return ''.join(res)
class Solution2:
    # https://www.youtube.com/watch?v=zaM_GLLvysw
    def reorganizeString(self, S):
        n = len(S)
        counter = Counter(S)
        pq = []
        res = []
        for letter in counter:
            pq.append((-counter[letter], letter))

        for count in counter.values():
            if count>(n+1)//2:
                return ""
        heapify(pq)
        while len(pq)>1:
            current = heappop(pq)
            curr_cnt, curr_char = current[0]*(-1), current[1] # -1 for min heap
            next = heappop(pq)
            next_cnt, next_char = next[0]*(-1), next[1] # -1 for min heap
            res.append(curr_char)
            res.append(next_char)
            curr_cnt-=1
            next_cnt -=1
            if curr_cnt>0: # - for min heap
                heappush(pq, (-curr_cnt, curr_char)) # - for min heap
            if next_cnt>0:
                heappush(pq, (-next_cnt, next_char))
        if pq:
            lastcount, lastchar = heappop(pq)
            if -(lastcount)>1:
                return ""
            res.append(lastchar)
        return "".join(res)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual("aba", get_sol().reorganizeString("aab"))
    def test_2(self):
        self.assertEqual("", get_sol().reorganizeString("aaab"))
    def test_3(self):
        self.assertEqual("vlvov", get_sol().reorganizeString("vvvlo"))
    def test_4(self):
        self.assertEqual("", get_sol().reorganizeString("bbbbbbb"))
    def test_5(self):
        self.assertEqual("wbwdgkopwzabdegkopsvwyzabdefgijklmnopqrsuvwyz", get_sol().reorganizeString("zqugrfbsznyiwbokwkpvpmeyvaosdkedbgjogzdpwawwl"))
    def test_6(self):
        self.assertEqual("", get_sol().reorganizeString("snywkvpmeyvaosdkedbgjogzdpwawwl"))
    def test_7(self):
        self.assertEqual("", get_sol().reorganizeString("snywkvpmvaoskedbgjogzdpwawwl"))
    def test_8(self):
        self.assertEqual("", get_sol().reorganizeString("snywkvpmvaoskedbgj"))
    def test_9(self):
        self.assertEqual("", get_sol().reorganizeString("kkkkzrkatkwpkkkktrq"))


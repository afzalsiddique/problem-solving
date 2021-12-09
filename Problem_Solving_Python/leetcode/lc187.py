import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def myord(ch):
            if ch=='A': return 1
            if ch=='C': return 2
            if ch=='G': return 3
            return 4

        m=len(s)
        if m<11: return []
        h=1
        prime=10**8+7
        di={}
        base=4
        n=10
        for i in range(n-1):
            h=(h*base) % prime
        t=0 # rolling hash of window
        for i in range(n):
            t=(t*base+myord(s[i])) % prime
        for i in range(m-n+1):
            if t not in di:
                di[t]=[0,-1] # cnt, index
            di[t]=[di[t][0]+1,i]
            t=t-myord(s[i])*h
            if i+n<m:
                t=(t*base+myord(s[i+n])) % prime
            if t<0:
                t+=prime

        res=[]
        for key in di:
            if di[key][0]>1:
                start=di[key][1]
                res.append(s[start:start+10])
        return res

class Solution2:
    # time O(10*len(DNA)). space O(len(DNA)/10)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di=defaultdict(int)
        res=[]
        for i in range(len(s)-10+1):
            di[s[i:i+10]]+=1
        for seq in di:
            if di[seq]>1: res.append(seq)
        return res
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(["AAAAACCCCC","CCCCCAAAAA"],get_sol().findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    def test2(self):
        self.assertEqual(["AAAAAAAAAA"],get_sol().findRepeatedDnaSequences(s = "AAAAAAAAAAAAA"))
    def test3(self):
        self.assertEqual([],get_sol().findRepeatedDnaSequences(s = "A"))
    # def test4(self):
    #     self.assertEqual(Output,get_sol().findRepeatedDnaSequences(s = "banana"))

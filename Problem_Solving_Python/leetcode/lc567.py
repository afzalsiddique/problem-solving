import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2: return False
        di1={c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        di2={c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        for c in s1:
            di1[c]+=1
        i=0
        while i<n1:
            di2[s2[i]]+=1
            i+=1
        while i<n2:
            if di1==di2: return True
            di2[s2[i]]+=1
            di2[s2[i-n1]]-=1
            i+=1
        if di1==di2: return True
        return False

class tester(unittest.TestCase):
    def test1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        Output= True
        self.assertEqual(Output,Solution().checkInclusion(s1,s2))
    def test2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        Output= False
        self.assertEqual(Output,Solution().checkInclusion(s1,s2))
    def test3(self):
        s1 = "adc"
        s2 = "dcda"
        Output= True
        self.assertEqual(Output,Solution().checkInclusion(s1,s2))
    def test4(self):
        s1 = "ab"
        s2 = "ba"
        Output= True
        self.assertEqual(Output,Solution().checkInclusion(s1,s2))

import itertools;from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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

class Tester(unittest.TestCase):
    def test01(self):
        s1,s2 = "ab" ,"eidbaooo"
        self.assertEqual(True,get_sol().checkInclusion(s1,s2))
    def test02(self):
        s1,s2 = "ab" ,"eidboaoo"
        self.assertEqual(False,get_sol().checkInclusion(s1,s2))
    def test03(self):
        s1,s2 = "adc" ,"dcda"
        self.assertEqual(True,get_sol().checkInclusion(s1,s2))
    def test04(self):
        s1,s2 = "ab" ,"ba"
        self.assertEqual(True,get_sol().checkInclusion(s1,s2))
    def test05(self):
        s1,s2 = "horse" ,"ors"
        self.assertEqual(False,get_sol().checkInclusion(s1,s2))

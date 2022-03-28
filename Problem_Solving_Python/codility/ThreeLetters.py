from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
def solution(A,B):
    return helper('a',A,'b',B)
def helper(a, cntA, b, cntB):
    if cntB>cntA:
        return helper(b, cntB, a, cntA)
    if not cntB:
        return a*cntA
    res=[]
    while cntA>cntB and cntA>=2 and cntB>=1:
        res.append(a)
        res.append(a)
        res.append(b)
        cntA-=2
        cntB-=1
    while cntA and cntB and cntA==cntB:
        res.append(a)
        res.append(b)
        cntA-=1
        cntB-=1
    if not cntA and not cntB:
        return ''.join(res)
    return ''.join(res)+helper(a,cntA,b,cntB)

def test(s):
    cnt=0
    prev='#'
    for c in s:
        cnt=cnt+1 if c==prev else 0
        if cnt==3: return False
        prev=c
    return True
class Tester(unittest.TestCase):
    def test01(self):
        self.assertTrue(test(solution(5,3)))
    def test02(self):
        self.assertTrue(test(solution(1,4)))
    def test03(self):
        self.assertTrue(test(solution(0,0)))
    def test04(self):
        self.assertTrue(test(solution(2,0)))
    def test05(self):
        self.assertTrue(test(solution(3,3)))
    def test06(self):
        self.assertTrue(test(solution(4,3)))
    def test07(self):
        self.assertTrue(test(solution(3,4)))
    def test08(self):
        self.assertTrue(test(solution(8,3)))
    def test09(self):
        self.assertTrue(test(solution(3,8)))
    def test10(self):
        self.assertTrue(test(solution(8,8)))
    def test11(self):
        self.assertTrue(test(solution(1,3)))
    def test12(self):
        self.assertTrue(test(solution(2,3)))
    def test13(self):
        self.assertTrue(test(solution(0,1)))
    def test14(self):
        self.assertTrue(test(solution(0,2)))
    def test15(self):
        self.assertTrue(test(solution(2,4)))
    def test16(self):
        self.assertTrue(test(solution(3,1)))

import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canTransform(self, start, end)->bool:
        n=len(start)
        i,j=0,0
        while i<n or j<n:
            while i<n and start[i]=='X': i+=1
            while j<n and end[j]=='X': j+=1
            if i==n and j==n: return True
            if i==n or j==n: return False
            if start[i]!=end[j]: return False
            if start[i]=='L' and i<j: return False
            if start[i]=='R' and i>j: return False
            i+=1
            j+=1
        return True
class Solution2:
    def canTransform(self, start, end)->bool:
        start=start+"X"
        end=end+"X"
        n=len(start)
        i,j=0,0
        while i<n and j<n:
            while i<n and start[i]=='X': i+=1
            while j<n and end[j]=='X': j+=1
            if i==n and j==n: return True
            if i==n or j==n: return False
            if start[i]!=end[j]: return False
            if start[i]=='L' and i<j: return False
            if start[i]=='R' and i>j: return False
            i+=1
            j+=1
        return True
class Solution3:
    # wrong
    def canTransform(self, start: str, end: str) -> bool:
        n=len(start)
        def helper(i):
            if i==n: return True
            if start[i]==end[i]:
                if helper(i+1): return True
            if i==n-1: return False
            if start[i:i+2]=='RX' and end[i:i+2]=='XR':
                if helper(i+2): return True
            if start[i:i+2]=='XL' and end[i:i+2]=='LX':
                if helper(i+2): return True
            return False

        return helper(0)

class MyTestCase(unittest.TestCase):
    def test_01(self):
        start = "RXXLRXRXL"
        end = "XRLXXRRLX"
        Output= True
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_02(self):
        start = "X"
        end = "L"
        Output= False
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_03(self):
        start = "LLR"
        end = "RRL"
        Output= False
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_04(self):
        start = "XL"
        end = "LX"
        Output= True
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_05(self):
        start = "XLLR"
        end = "LXLX"
        Output= False
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_06(self):
        start = "XXXXXLXXXX"
        end = "LXXXXXXXXX"
        Output= True
        self.assertEqual(Output,get_sol().canTransform(start,end))
    def test_07(self):
        start = "RXR"
        end = "XXR"
        Output= False
        self.assertEqual(Output,get_sol().canTransform(start,end))

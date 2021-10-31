import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def ones_at_beginning(b:str):
            for i in range(8):
                if b[i]=='0': return i
            return i

        li=[]
        for x in data:
            b = bin(x)[2:]
            if len(b)<8: b = '0'*(8-len(b))+b
            li.append(b)
        n=len(data)
        i=0
        while i<n:
            b=li[i]
            ones = ones_at_beginning(b)
            if ones==1: return False # can't start a char with '10'
            if ones>4: return False # maximum 4 bytes
            ones -=1 # remaining bytes
            while i+1<n and ones>0 and ones_at_beginning(li[i+1])==1:
                i+=1
                ones-=1
            if ones>0: return False
            i+=1
        return True

class MyTestCase(unittest.TestCase):
    def test1(self):
        data = [197,130,1]
        Output= True
        self.assertEqual(Output, get_sol().validUtf8(data))
    def test2(self):
        data = [235,140,4]
        Output= False
        self.assertEqual(Output, get_sol().validUtf8(data))
    def test3(self):
        data = [10]
        Output= True
        self.assertEqual(Output, get_sol().validUtf8(data))
    def test4(self):
        data = [145]
        Output= False
        self.assertEqual(Output, get_sol().validUtf8(data))
    def test5(self):
        data = [240,162,138,147,145]
        Output= False
        self.assertEqual(Output, get_sol().validUtf8(data))
    def test6(self):
        data = [250,145,145,145,145]
        Output= False
        self.assertEqual(Output, get_sol().validUtf8(data))
    # def test7(self):

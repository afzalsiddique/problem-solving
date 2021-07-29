import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation
    def minimumSwap(self, s1: str, s2: str) -> int:
        n=len(s1)
        x_y,y_x=0,0
        for i in range(n):
            if s1[i]=='x' and s2[i]=='y': x_y+=1
            if s1[i]=='y' and s2[i]=='x': y_x+=1
        if (x_y+y_x)%2: return -1
        return x_y//2 + y_x//2 + x_y%2 + y_x%2



class tester(unittest.TestCase):
    def test_1(self):
        s1,s2= "xx","yy"
        Output= 1
        self.assertEqual(Output,get_sol().minimumSwap(s1,s2))
    def test_2(self):
        s1,s2= "xy","yx"
        Output= 2
        self.assertEqual(Output,get_sol().minimumSwap(s1,s2))
    def test_3(self):
        s1,s2= "xx","xy"
        Output= -1
        self.assertEqual(Output,get_sol().minimumSwap(s1,s2))
    def test_4(self):
        s1,s2= "xxyyxyxyxx","xyyxyxxxyx"
        Output= 4
        self.assertEqual(Output,get_sol().minimumSwap(s1,s2))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid(txt:str):
            before,after=txt.split('.') # before decimal and after decimal
            if after[-1]=='0': return False # last digit after decimal can not be zero
            if len(before)>=2 and before[0]=='0': return False # first digit can not be '0' except '0' itself
            return True
        def h(txt:str):
            if len(txt)==1: return [txt]
            if set(txt)=={'0'}: return []
            res=[]
            if len(txt)>=2 and txt[0]!= '0': # first digit can not be '0' except '0' itself
                res.append(txt)
            for i in range(len(txt) - 1):
                tmp= txt[:i + 1] + '.' + txt[i + 1:]
                if valid(tmp):
                    res.append(tmp)
            return res

        res=[]
        s=s[1:-1] # remove the extra parenthesis
        for i in range(len(s)-1):
            first=s[:i+1]
            second=s[i+1:]
            li1=h(first)
            li2=h(second)
            for x in li1:
                for y in li2:
                    res.append('('+x+', '+y+')')
        return res
class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "(123)"
        Output= ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
        self.assertEqual(sorted(Output), sorted(get_sol().ambiguousCoordinates(s)))
    def test_2(self):
        s = "(0123)"
        Output= ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
        self.assertEqual(sorted(Output), sorted(get_sol().ambiguousCoordinates(s)))
    def test_3(self):
        s = "(00011)"
        Output= ["(0, 0.011)","(0.001, 1)"]
        self.assertEqual(sorted(Output), sorted(get_sol().ambiguousCoordinates(s)))
    def test_4(self):
        s = "(100)"
        Output= ["(10, 0)"]
        self.assertEqual(sorted(Output), sorted(get_sol().ambiguousCoordinates(s)))
    def test_5(self):
        s = "(0010)"
        Output= ["(0.01, 0)"]
        self.assertEqual(sorted(Output), sorted(get_sol().ambiguousCoordinates(s)))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

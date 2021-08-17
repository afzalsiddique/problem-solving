import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        n=len(s)
        di=defaultdict(lambda :'?')
        for key,val in knowledge:
            di[key]=val
        res=[]
        i=0
        while i<n:
            if s[i]=='(':
                i+=1
                start=i
                while i<n and s[i]!=')':
                    i+=1
                key=s[start:i]
                res.append(di[key])
            else:
                res.append(s[i])
            i+=1
        return ''.join(res)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s,knowledge = "(name)is(age)yearsold", [["name","bob"],["age","two"]]
        Output= "bobistwoyearsold"
        self.assertEqual(Output, get_sol().evaluate(s,knowledge))
    def test_2(self):
        s,knowledge = "hi(name)", [["a","b"]]
        Output= "hi?"
        self.assertEqual(Output, get_sol().evaluate(s,knowledge))
    def test_3(self):
        s,knowledge = "(a)(a)(a)aaa", [["a","yes"]]
        Output= "yesyesyesaaa"
        self.assertEqual(Output, get_sol().evaluate(s,knowledge))
    def test_4(self):
        s,knowledge = "(a)(b)", [["a","b"],["b","a"]]
        Output= "ba"
        self.assertEqual(Output, get_sol().evaluate(s,knowledge))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
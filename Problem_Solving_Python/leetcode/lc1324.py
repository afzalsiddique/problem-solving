import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def printVertically(self, s: str) -> List[str]:
        strs = s.split()
        col= len(strs)
        row=len(max(strs,key=len))
        res = [[' ' for __ in range(col)] for _ in range(row)]
        # print(row)
        # print(col)
        # print(strs)
        # print(res)
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                res[j][i]=strs[i][j]
        for i in range(len(res)):
            li=res[i]
            while li and li[-1]==' ':
                li.pop()
        res=[''.join(x) for x in res]
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "HOW ARE YOU"
        Output= ["HAY","ORO","WEU"]
        self.assertEqual(Output,get_sol().printVertically(s))
    def test2(self):
        s = "TO BE OR NOT TO BE"
        Output= ["TBONTB","OEROOE","   T"]
        self.assertEqual(Output,get_sol().printVertically(s))
    def test3(self):
        s = "CONTEST IS COMING"
        Output= ["CIC","OSO","N M","T I","E N","S G","T"]
        self.assertEqual(Output,get_sol().printVertically(s))
    # def test4(self):
    # def test5(self):
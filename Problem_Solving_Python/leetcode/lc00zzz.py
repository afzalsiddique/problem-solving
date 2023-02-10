from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res1,res2=0,0
        bal = 0
        for c in s:
            if bal<0:
                res1=max(res1,abs(bal))
            if c=='(':
                bal+=1
            else:
                bal-=1
        res1=max(res1,abs(bal))

        bal=0
        for c in s[::-1]:
            if bal>0:
                res2=max(res2,bal)
            if c=='(':
                bal+=1
            else:
                bal-=1
        res2=max(res2,abs(bal))

        # return res1+res2
        return min(res1,res2)

class MyTestCase(unittest.TestCase):
    def test01(self):
        Input= "())"
        Output= 1
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test02(self):
        Input= "((("
        Output= 3
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test03(self):
        Input= "()"
        Output= 0
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test04(self):
        Input= "()))(("
        Output= 4
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test05(self):
        Input= "(()())(("
        Output= 2
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test06(self):
        Input= "()(("
        Output= 2
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))
    def test07(self):
        Input= "))()"
        Output= 2
        self.assertEqual(Output, get_sol().minAddToMakeValid(Input))

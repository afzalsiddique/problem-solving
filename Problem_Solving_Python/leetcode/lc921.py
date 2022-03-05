from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[] # st could be replaced with a variable. because only contains one type of character '('
        cnt=0
        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st: st.pop()
                else: cnt+=1
        return cnt+len(st)
class Solution3:
    def minAddToMakeValid(self, s: str) -> int:
        res=0

        left=0
        for c in s:
            if c=='(':
                left+=1
            else:
                if left:
                    left-=1
                else:
                    res+=1

        right=0
        for c in s[::-1]:
            if c==')':
                right+=1
            else:
                if right:
                    right-=1
                else:
                    res+=1
        return res
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        def helper(s,char):
            res=0

            balance=0
            for c in s:
                if c==char:
                    balance+=1
                else:
                    if balance:
                        balance-=1
                    else:
                        res+=1
            return res

        return helper(s,'(')+helper(s[::-1],')')

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

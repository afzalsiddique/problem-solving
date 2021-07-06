import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n=len(s)
        st=[]
        for i in range(n):
            if s[i]=='(':
                st.append(s[i])
            elif s[i]==')':
                tmp=[]
                while st[-1]!='(':
                    tmp.append(st.pop())
                st.pop()
                st.extend(tmp)
            else:
                st.append(s[i])
        # print(st)
        return ''.join(st)

class tester(unittest.TestCase):
    def test_1(self):
        s = "(abcd)"
        Output= "dcba"
        self.assertEqual(Output,get_sol().reverseParentheses(s))
    def test_2(self):
        s = "(u(love)i)"
        Output= "iloveu"
        self.assertEqual(Output,get_sol().reverseParentheses(s))
    def test_3(self):
        s = "(ed(et(oc))el)"
        Output= "leetcode"
        self.assertEqual(Output,get_sol().reverseParentheses(s))
    def test_4(self):
        s = "a(bcdefghijkl(mno)p)q"
        Output= "apmnolkjihgfedcbq"
        self.assertEqual(Output,get_sol().reverseParentheses(s))
    # def test_5(self):
    # def test_6(self):

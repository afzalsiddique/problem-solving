from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        n=len(s)
        li=[]
        j=0
        sign='+'
        while j<n:
            x=s[j]
            i=j
            while j<n and '0'<=s[j]<='9':
                j+=1
            num=s[i:j]
            if num:
                li.append(sign)
                li.append(num)
            if j<n:
                if s[j]=='+':
                    sign='+'
                elif s[j]=='-':
                    sign='-'
                elif s[j]=='(':
                    li.append(sign)
                    li.append(s[j])
                    sign='+' # reinitialize sign to be positive
                elif s[j]==')':
                    li.append(s[j])
                j+=1

        i=0
        st=[]
        sign2='+'
        num2=0
        while i<len(li):
            if li[i]!=')':
                st.append(li[i])
            else:
                tmp=0
                while st and st[-1]!='(':
                    num2=int(st.pop())
                    sign2=st.pop()
                    tmp+=num2*(1 if sign2=='+' else -1)
                if st and st[-1]=='(':
                    st.pop() # '('
                    sign2=st.pop()
                    st.append(sign2)
                    st.append(tmp)
            i+=1

        res=0
        while st:
            num3=int(st.pop())
            sign3=st.pop()
            res+=num3*(1 if sign3=='+' else -1)
        return res
class Solution2:
    # leetcode original
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                num = (num * 10) + int(ch)
            elif ch == '+':
                res += sign * num
                sign = 1
                num = 0
            elif ch == '-':
                res += sign * num
                sign = -1
                num = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * num
                res *= stack.pop() # stack pop 1, sign
                res += stack.pop() # stack pop 2, num
                num = 0
        return res + sign * num


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().calculate("1 + 1"))
    def test02(self):
        self.assertEqual(3,get_sol().calculate(" 2-1 + 2 "))
    def test03(self):
        self.assertEqual(23,get_sol().calculate("(1+(4+5+2)-3)+(6+8)"))
    def test04(self):
        self.assertEqual(0,get_sol().calculate(" "))
    def test05(self):
        self.assertEqual(0,get_sol().calculate("    "))
    def test06(self):
        self.assertEqual(1,get_sol().calculate(" 1"))
    def test07(self):
        self.assertEqual(-12,get_sol().calculate("- (3 + (4 + 5))"))
    def test08(self):
        self.assertEqual(2147483647,get_sol().calculate("2147483647"))
    def test09(self):
        self.assertEqual(22,get_sol().calculate("11 + 11"))
    def test10(self):
        self.assertEqual(12,get_sol().calculate("(3 + (4 + 5))"))
    def test11(self):
        self.assertEqual(7,get_sol().calculate("(1+(4+5)-3)"))
    def test12(self):
        self.assertEqual(-47,get_sol().calculate("(1-(40+5)-3)"))
    def test13(self):
        self.assertEqual(-1,get_sol().calculate("-2+ 1"))
    def test14(self):
        self.assertEqual(-3,get_sol().calculate("-(2+1)"))

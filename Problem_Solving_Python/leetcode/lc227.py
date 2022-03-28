import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # without stack
    def calculate(self, s: str) -> int:
        cur = 0
        prev=0
        result=0
        sign='+'
        s += '+'
        for c in s:
            if c == ' ': continue
            if c.isdigit():
                cur = 10 * cur + int(c)
                continue
            if sign == '+':
                result += prev
                prev = cur
            elif sign == '-':
                result += prev
                prev = -cur
            elif sign == '*':
                prev = prev * cur
            elif sign == '/':
                prev = int(prev / cur)
            cur, sign = 0, c
        return result + prev
class Solution6:
    # no stack but simulates stack
    def calculate(self, s: str) -> int:
        prevSign='+'
        prev=0
        res=0
        num=0
        for i in range(len(s)+1):
            if i<len(s) and s[i]==' ':
                continue
            if i<len(s) and '0'<=s[i]<='9':
                num=num*10+int(s[i])
            else:
                if prevSign=='+':
                    prev=num
                elif prevSign=='-':
                    prev=-num
                elif prevSign=='*':
                    res-=prev
                    prev=num*prev
                else:
                    res-=prev
                    sign=1 if prev>0 else -1
                    prev=abs(prev)
                    prev=(prev//num)*sign
                res+=prev
                num=0
                if i<len(s): prevSign=s[i]
        return res
class Solution4:
    # one iteration and stack
    def calculate(self, s: str) -> int:
        st=[]
        prevSign='+'
        num=0
        for i in range(len(s)+1):
            if i<len(s) and s[i]==' ':
                continue
            if i<len(s) and '0'<=s[i]<='9':
                num=num*10+int(s[i])
            else:
                if prevSign=='+':
                    st.append(num)
                elif prevSign=='-':
                    st.append(-num)
                elif prevSign=='*':
                    st.append(st.pop()*num)
                else:
                    last=st.pop()
                    sign=1 if last>0 else -1
                    last=abs(last)
                    tmp=last//num
                    st.append(tmp*sign)
                num=0
                if i<len(s): prevSign=s[i]
        return sum(st)
class Solution5:
    # stack and replace
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        s=s+"+"
        st,prev_sign,num = [],'+',0
        for c in s:
            if c.isdigit():
                num=num*10+ord(c)-ord('0')
            else:
                if prev_sign=='+':
                    st.append(num)
                elif prev_sign=='-':
                    st.append(-num)
                elif prev_sign=='*':
                    st.append(st.pop()*num)
                elif prev_sign=='/':
                    last_num = st.pop()
                    if last_num>0:
                        st.append(last_num//num)
                    else:
                        last_num = -last_num
                        ans = last_num//num
                        st.append(-ans)
                num=0
                prev_sign=c
        return sum(st)

class Solution3:
    def calculate(self, s: str) -> int:
        def removeSpaces(s:str):
            i=0
            li=[]
            while i<len(s):
                if s[i]!=' ':
                    li.append(s[i])
                i+=1
            return ''.join(li)
        def makeList(s:str):
            n=len(s)
            i=0
            li=[]
            while i<n:
                j=i
                while j<n and '0'<=s[j]<='9':
                    j+=1
                li.append(s[i:j])
                if j<n:
                    li.append(s[j])
                i=j+1
            return li

        s=removeSpaces(s)
        li=makeList(s)
        st=[]
        sign='+'
        for x in li:
            if x in '+-/*':
                sign=x
                continue
            if sign=='+':
                st.append(int(x))
            elif sign=='-':
                st.append(int(x)*(-1))
            elif sign=='*':
                st.append(int(x)*st.pop())
            elif sign=='/':
                prev=st.pop()
                lastNeg=-1 if prev<0 else 1
                prev=abs(prev)
                cur=prev//int(x)
                cur*=lastNeg
                st.append(cur)

        return sum(st)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(7,get_sol().calculate('3+2*2'))
    def test2(self):
        self.assertEqual(13,get_sol().calculate("14-3/2"))
    def test3(self):
        self.assertEqual(28,get_sol().calculate("2+5+7*3"))
    def test4(self):
        self.assertEqual(17,get_sol().calculate("2+5+10"))
    def test5(self):
        self.assertEqual(-14,get_sol().calculate("2+5-7*3"))
    def test6(self):
        self.assertEqual(1,get_sol().calculate(" 3/2 "))

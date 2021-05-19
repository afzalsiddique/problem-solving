import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution2()
class Solution:
    # time O(n) space O(n)
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        st.append(0)
        for c in s:
            if c =='(':
                st.append(0)
            else:
                top=st.pop()
                second_top=st.pop()
                tmp=second_top+max(top*2,1)
                st.append(tmp)
        return st.pop()


class Solution2:
    # time O(n) space O(1)
    def scoreOfParentheses(self, s: str) -> int:
        res=0
        l=0
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            else:
                l-=1
            if s[i]==')' and s[i-1]=='(':
                res+=2**l
        return res
class Solution3:
    # time O(n) space O(n)
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        for c in s:
            if c=='(':
                st.append(-1)
            else:
                cur=0
                while st[-1]!=-1:
                    cur+=st.pop()
                st.pop()
                if cur==0:
                    st.append(1)
                else:
                    st.append(cur*2)
        ans=0
        while st:
            ans+=st.pop()
        return ans
class tester(unittest.TestCase):
    def test1(self):
        s = "()"
        Output= 1
        self.assertEqual(Output,get_sol().scoreOfParentheses(s))
    def test2(self):
        s = "(())"
        Output= 2
        self.assertEqual(Output,get_sol().scoreOfParentheses(s))
    def test3(self):
        s = "()()"
        Output= 2
        self.assertEqual(Output,get_sol().scoreOfParentheses(s))
    def test4(self):
        s = "(()(()))"
        Output= 6
        self.assertEqual(Output,get_sol().scoreOfParentheses(s))
    def test5(self):
        s = "(()((())))"
        Output= 10
        self.assertEqual(Output,get_sol().scoreOfParentheses(s))

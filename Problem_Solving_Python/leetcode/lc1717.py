import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.helper(s,x,y,'ab','ba')
    def helper(self, s:str, x:int, y:int, x_txt:str, y_txt:str):
        if y>x: return self.helper(s, y, x, y_txt, x_txt)
        st=[]
        res = 0
        for i in range(len(s)):
            st.append(s[i])
            if len(st)>=2 and st[-2]==x_txt[0] and st[-1]==x_txt[1]:
                st.pop()
                st.pop()
                res+=x

        new_s = ''.join(st)
        st=[]
        for i in range(len(new_s)):
            st.append(new_s[i])
            if len(st)>=2 and st[-2]==y_txt[0] and st[-1]==y_txt[1]:
                st.pop()
                st.pop()
                res+=y

        return res



class MyTestCase(unittest.TestCase):
    def test1(self):
        s,x,y = "cdbcbbaaabab",  4,  5
        Output= 19
        self.assertEqual(Output, get_sol().maximumGain(s,x,y))
    def test2(self):
        s,x,y= "aabbaaxybbaabb",5, 4
        Output= 20
        self.assertEqual(Output, get_sol().maximumGain(s,x,y))
    # def test3(self):
    # def test4(self):
    # def test5(self):
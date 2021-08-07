import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def clumsy(self, n: int) -> int:
        signs=['*','/',1,-1]
        s_i=0
        st=[n]
        for num in range(n-1,0,-1):
            sign=signs[s_i]
            if sign=='*':
                st.append(st.pop()*num)
            elif sign=='/':
                if st[-1]*num<0: # ans will be negative
                    st.append( abs(st.pop()) // abs(num) )
                    st[-1] *= (-1) # make it negative
                else:
                    st.append(st.pop()//num)
            else:
                st.append(num*sign)
            s_i=(s_i+1)%4
        return sum(st)
class Tester(unittest.TestCase):
    def test_1(self):
        n = 4
        Output= 7
        self.assertEqual(Output,get_sol().clumsy(n))
    def test_2(self):
        n = 10
        Output= 12
        self.assertEqual(Output,get_sol().clumsy(n))
    def test_3(self):
        n = 7
        Output= 6
        self.assertEqual(Output,get_sol().clumsy(n))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def solveEquation(self, equation: str) -> str:
        def func(li, sign):
            li = li + "+"
            if li[0]=='-':
                li = '0'+li
            n=len(li)
            i,j=0,0
            x_val,val = 0,0
            while i<n:
                if li[i]=='+' or li[i]=='-':
                    tmp = li[j:i]
                    if tmp=='+x' or tmp=='x':
                        tmp='+1x'
                    elif tmp=='-x':
                        tmp='-1x'
                    if tmp[-1]=='x':
                        x_val+= int(tmp[:-1]) * sign
                    else:
                        val += int(tmp) * sign
                    j=i
                i+=1

            # print(const, coeff)
            return x_val,val

        left,right = equation.split('=')
        coeff,const = func(left,1)
        coeff_tmp, const_tmp = func(right,-1)
        coeff += coeff_tmp
        const += const_tmp
        if coeff==0 and const!=0: return "No solution"
        if coeff==0: return "Infinite solutions"
        res = const/coeff*(-1)
        res = int(res)
        return 'x='+str(res)

class MyTestCase(unittest.TestCase):
    def test1(self):
        equation = "x+5-3+x=6+x-2"
        Output= "x=2"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    def test2(self):
        equation = "x=x"
        Output= "Infinite solutions"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    def test3(self):
        equation = "2x=x"
        Output= "x=0"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    def test4(self):
        equation = "2x+3x-6x=x+2"
        Output= "x=-1"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    def test5(self):
        equation = "x=x+2"
        Output= "No solution"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    def test6(self):
        equation = "-x=-1"
        Output= "x=1"
        self.assertEqual(Output, get_sol().solveEquation(equation))
    # def test7(self):

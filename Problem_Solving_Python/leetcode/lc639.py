from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution2()
class Solution:
    def numDecodings(self, s: str) -> int:
        M=10**9+7
        def get_two_digits(i:int):
            # if i+1>=n: return 0
            # if s[i]=='0': return 0
            # if s[i]>='3': return 0
            if s[i]==s[i+1]=='*': return 15
            if s[i]=='*':
                if '0'<=s[i+1]<='6':
                    return 2
                else:
                    return 1
            elif s[i+1]=='*':
                if s[i]=='1':
                    return 9
                elif s[i]=='2':
                    return 6
                return 0
            return 1
        def get_one_digit(i:int):
            if s[i]=='*': return 9
            return 1
        @cache
        def dfs(i):
            if i>=n: return 1
            if s[i]=='0': return 0
            ans1=get_one_digit(i)
            ans2=dfs(i+1)
            ans3,ans4=0,0
            if i+1<n:
                if s[i]=='*' or s[i+1]=='*':
                    ans3=get_two_digits(i)
                    ans4=dfs(i+2)
                elif s[i]=='1' or s[i]=='2' and s[i+1]<='6':
                    ans3=1
                    ans4=dfs(i+2)
            res=ans1*ans2+ans3*ans4
            return res%M

        n=len(s)
        return dfs(0)
class Solution2:
    def get_two_digits(self,s:str):
        if s=='**': # 11-19, 21-26. because * in in the range [1-9]
            return 15
        if s[0]=='*':
            if '0'<=s[1]<='6':
                # *0 -> 10, 20
                # *1 -> 11, 21
                # *6 -> 16, 26
                return 2
            else:
                # *7 -> 17
                return 1
        if s[1]=='*':
            if s[0]=='1':
                # 1* -> 11,12,13,...19
                return 9
            if s[0]=='2':
                # 2* -> 21,22,...26
                return 6

            # 3* -> invalid
            return 0
    def numDecodings(self, s: str) -> int:
        # di = {}
        # di["**"]=15 # 11-19, 21-26
        # di["*0"]=2 # 1,2
        # di["*1"]=2
        # di["*2"]=2
        # di["*3"]=2
        # di["*4"]=2
        # di["*5"]=2
        # di["*6"]=2
        # di["*7"]=1 # 1
        # di["*8"]=1
        # di["*9"]=1
        # di["1*"]=9 # 1-9
        # di["2*"]=6 # 1-6
        # di["3*"]=0
        # di["4*"]=0
        # di["5*"]=0
        # di["6*"]=0
        # di["7*"]=0
        # di["8*"]=0
        # di["9*"]=0

        @cache
        def func(i):
            if i==n: return 1
            if s[i]=='0': return 0 # can not start a number with zero
            # take one digit
            if s[i]=='*':
                ans=9
            else:
                ans=1
            ans*=func(i+1)
            # take two digits
            if i<n-1:
                s2=s[i:i+2]
                if '*' in s2:
                    ans+=self.get_two_digits(s2)*func(i+2)
                elif s[i]=='1' or s[i]=='2' and s[i+1]<'7':
                    ans+=func(i+2)
                ans%=mod
            return ans


        n=len(s)
        mod=10**9+7
        return func(0)



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(9, get_sol().numDecodings(s = "*"))
    def test2(self):
        self.assertEqual(18, get_sol().numDecodings(s = "1*"))
    def test3(self):
        self.assertEqual(15, get_sol().numDecodings(s = "2*"))
    def test4(self):
        self.assertEqual(11, get_sol().numDecodings(s="*1"))
    def test5(self):
        self.assertEqual(2, get_sol().numDecodings(s="*0"))
    def test6(self):
        self.assertEqual(11, get_sol().numDecodings(s="*3"))
    def test7(self):
        self.assertEqual(999, get_sol().numDecodings(s="***"))
    def test8(self):
        self.assertEqual(9, get_sol().numDecodings(s="3*"))
    def test9(self):
        self.assertEqual(11859129, get_sol().numDecodings(s="*******"))
    def test10(self):
        self.assertEqual(96, get_sol().numDecodings(s="**"))
    def test11(self):
        self.assertEqual(882201566, get_sol().numDecodings(s="1*6*7*1*9*6*2*9*2*3*3*6*3*2*2*4*7*2*9*6*0*6*4*4*1*6*9*0*5*9*2*5*7*7*0*6*9*7*1*5*5*9*3*0*4*9*2*6*2*5*7*6*1*9*4*5*8*4*7*4*2*7*1*2*1*9*1*3*0*6*"))
    def test12(self):
        self.assertEqual(1, get_sol().numDecodings("2839"))
    def test91(self):
        self.assertEqual(2,get_sol().get_two_digits("*0"))
    def test92(self):
        self.assertEqual(2,get_sol().get_two_digits("*1"))
    def test93(self):
        self.assertEqual(2,get_sol().get_two_digits("*2"))
    def test94(self):
        self.assertEqual(2,get_sol().get_two_digits("*3"))
    def test95(self):
        self.assertEqual(2,get_sol().get_two_digits("*4"))
    def test96(self):
        self.assertEqual(2,get_sol().get_two_digits("*5"))
    def test97(self):
        self.assertEqual(2,get_sol().get_two_digits("*6"))
    def test98(self):
        self.assertEqual(1,get_sol().get_two_digits("*7"))
    def test99(self):
        self.assertEqual(1,get_sol().get_two_digits("*8"))
    def test910(self):
        self.assertEqual(1,get_sol().get_two_digits("*9"))
    def test911(self):
        self.assertEqual(9,get_sol().get_two_digits("1*"))
    def test912(self):
        self.assertEqual(6,get_sol().get_two_digits("2*"))
    def test913(self):
        self.assertEqual(0,get_sol().get_two_digits("3*"))
    def test914(self):
        self.assertEqual(0,get_sol().get_two_digits("4*"))
    def test915(self):
        self.assertEqual(0,get_sol().get_two_digits("5*"))
    def test916(self):
        self.assertEqual(0,get_sol().get_two_digits("6*"))
    def test917(self):
        self.assertEqual(0,get_sol().get_two_digits("7*"))
    def test918(self):
        self.assertEqual(0,get_sol().get_two_digits("8*"))
    def test919(self):
        self.assertEqual(0,get_sol().get_two_digits("9*"))
    def test920(self):
        self.assertEqual(15, get_sol().get_two_digits(s = "**"))

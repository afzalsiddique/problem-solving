from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
# def get_sol(): return Solution()
# class Solution:
def isWord(i, s, matchWord):
    n=len(s)
    j=0
    while i<n and j<len(matchWord) and s[i]==matchWord[j]:
        i+=1
        j+=1
    return j==len(matchWord)
def transformLanguage(s:str) -> str:
    n=len(s)
    i=0
    res=[]
    stack=[0]
    while i<n:
        if s[i]==' ':
            res.append(s[i])
            i+=1
        elif s[i]=='(':
            stack.append(0)
            res.append(s[i])
            i+=1
        elif s[i]==')':
            stack.pop()
            stack[-1]+=1
            res.append(s[i])
            i+=1
        elif isWord(i,s,'ebong'):
            if stack[-1]%2==0: # operand
                res.append('ebong')
            else:
                res.append('&&')
            stack[-1]+=1
            i+=5
        elif isWord(i,s,'othoba'):
            if stack[-1]%2==0: # operand
                res.append('othoba')
            else:
                res.append('||')
            stack[-1]+=1
            i+=6
        else:
            while i<n:
                if s[i] in [' ','(',')']:
                    break
                res.append(s[i])
                i+=1
            stack[-1]+=1
    return ''.join(res)



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("a || b",transformLanguage("a othoba b"))
    def test2(self):
        self.assertEqual("b && c || d",transformLanguage("b ebong c othoba d"))
    def test3(self):
        self.assertEqual("ebong && othoba || ebong",transformLanguage("ebong ebong othoba othoba ebong"))
    def test4(self):
        self.assertEqual("((ebong) || ebong) && othoba",transformLanguage("((ebong) othoba ebong) ebong othoba"))
    def test5(self):
        self.assertEqual("(ebong || (ebong && ((othoba)||(ebong))))",transformLanguage("(ebong othoba (ebong ebong ((othoba)othoba(ebong))))"))
    def test6(self):
        self.assertEqual("ebong",transformLanguage("ebong"))
    # def test7(self):
    # def test8(self):

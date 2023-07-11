from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def f(a:str, b:str):
            if a==b:
                return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
                print('pruning')
                return False
            for i in range(1, len(a)):
                aFirst=a[:i] # len i
                aLast=a[i:]
                bFirst=b[:i] # len i
                bLast=b[i:]
                bFirst2=b[:-i]
                bLast2=b[-i:] # len i
                if f(aFirst,bFirst) and f(aLast,bLast):
                    return True
                if f(aFirst,bLast2) and f(aLast,bFirst2):
                    return True
            return False

        return f(s1,s2)


class tester(unittest.TestCase):
    def test01(self):
        s1 = "great"
        s2 = "rgeat"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test02(self):
        s1 = "abcde"
        s2 = "caebd"
        Output= False
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test03(self):
        s1 = "a"
        s2 = "a"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test04(self):
        s1 = "abc"
        s2 = "bca"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))


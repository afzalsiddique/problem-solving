from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def helper(s1:str,s2:str)-> bool:
            if s1==s2: return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
                return False
            for i in range(1,len(s1)): # len(s1) is equal to len(s2)
                s1_first_i=s1[:i]
                s2_first_i=s2[:i]
                s2_skip_first_i=s2[i:]
                s2_last_i=s2[-i:]
                s1_skip_first_i,s2_skip_last_i=s1[i:],s2[:-i]

                # g | reat
                # r | geat
                # (g,r) and (reat,geat)
                if helper(s1_first_i,s2_first_i) and helper(s1_skip_first_i,s2_skip_first_i):
                    return True

                # g | reat
                # rgea | t
                # (g,t) and (reat,rgea)
                if helper(s1_first_i,s2_last_i) and helper(s1_skip_first_i,s2_skip_last_i): # swapping
                    return True
            return False

        return helper(s1,s2)

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


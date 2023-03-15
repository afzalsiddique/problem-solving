from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def recur(i,j):
            if i>j: return 0
            if i==j: return 1
            while i+1<=j and s[i]==s[i+1]:
                i+=1
            while j-1>=i and s[j]==s[j-1]:
                j-=1
            if s[i]!=s[j]:
                return 2+recur(i+1,j-1)
            return 1+recur(i+1,j-1)

        return recur(0,len(s)-1)



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().strangePrinter("abbb"))
    def test02(self):
        self.assertEqual(2, get_sol().strangePrinter("aaabbb"))
    def test03(self):
        self.assertEqual(2, get_sol().strangePrinter("aba"))
    def test04(self):
        self.assertEqual(1, get_sol().strangePrinter("bb"))
    def test05(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test06(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test07(self):
        self.assertEqual(14, get_sol().strangePrinter("abcdefghijklmn"))
    def test08(self):
        self.assertEqual(3, get_sol().strangePrinter("abbc"))
    def test09(self):
        self.assertEqual(7, get_sol().strangePrinter("abcabcabc"))
    def test10(self):
        self.assertEqual(5, get_sol().strangePrinter("abcabc"))

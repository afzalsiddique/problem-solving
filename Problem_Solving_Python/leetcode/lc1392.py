from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def longestPrefix(self, s: str) -> str:
        lps=self.getLps(s)
        return s[:lps[-1]]
    def getLps(self,txt):
        n=len(txt)
        lps=[0]*n
        i,j=0,1
        while j<n:
            if txt[i]==txt[j]:
                lps[j]=i+1
                i+=1
                j+=1
            else:
                if i==0:
                    j+=1
                else:
                    i=lps[i-1]
        return lps

class MyTestCase(unittest.TestCase):

    def test01(self):
        self.assertEqual('l', get_sol().longestPrefix("level"))
    def test02(self):
        self.assertEqual('abab', get_sol().longestPrefix("ababab"))
    def test03(self):
        self.assertEqual("ac", get_sol().longestPrefix("acccbaaacccbaac"))
    def test04(self):
        self.assertEqual("", get_sol().longestPrefix("a"))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):

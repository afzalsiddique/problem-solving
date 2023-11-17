from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def parseInt(i):
            if abbr[i]=='0': return None,None # zero at the beginning
            num=0
            while i<m and '0'<=abbr[i]<='9':
                num=num*10+int(abbr[i])
                i+=1
            return num,i
        m,n=len(abbr),len(word)
        i,j=0,0
        while j<n and i<m:
            if i<m and 'a'<=abbr[i]<='z':
                if word[j]!=abbr[i]:
                    return False
                i+=1
                j+=1
            else:
                num,i=parseInt(i)
                if (num,i)==(None,None): return False # zero at the beginning
                j+=num
        return i==m and j==n



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,get_sol().validWordAbbreviation("internationalization", "i12iz4n"))
    def test02(self):
        self.assertEqual(False,get_sol().validWordAbbreviation("apple", "a2e"))
    def test03(self):
        self.assertEqual(False,get_sol().validWordAbbreviation("a", "01"))
    # def test04(self):
    # def test05(self):
    # def test06(self):

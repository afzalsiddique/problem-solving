from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        res=[]
        l,r=0,len(s)-1
        hasMiddle=False
        while l<=r:
            if l==r:
                hasMiddle=True
                break
            if s[l]==s[r]:
                res.append(s[l])
                l+=1
                r-=1
            else:
                res.append(s[r])
                r-=1
        if not hasMiddle:
            res=res[:]+res[::-1]
        else:
            res=res[:]+[s[l]]+res[::-1]
        return ''.join(res)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("aaacecaaa",get_sol().shortestPalindrome("aacecaaa"))
    def test2(self):
        self.assertEqual("dcbabcd",get_sol().shortestPalindrome("abcd"))
    def test3(self):
        self.assertEqual("a",get_sol().shortestPalindrome("a"))
    def test4(self):
        self.assertEqual("",get_sol().shortestPalindrome(""))
    def test5(self):
        self.assertEqual("abbaabba",get_sol().shortestPalindrome("aabba"))

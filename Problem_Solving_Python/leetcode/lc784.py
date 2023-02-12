from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def letterCasePermutation(self, S: str):
        res = []
        my_str = []

        def make_list():
            for char in S:
                my_str.append(char)

        def backtrack(i):
            if i == len(my_str):
                res.append("".join(my_str))
                return
            if '0' <= my_str[i] <= '9':
                backtrack(i + 1)
            else:
                my_str[i] = my_str[i].lower()
                backtrack(i + 1)
                my_str[i] = my_str[i].upper()
                backtrack(i + 1)

        make_list()
        backtrack(0)
        return res

class Solution2:
    def letterCasePermutation(self, s: str) -> List[str]:
        def isLetter(i): return not '0'<=s[i]<='9'
        def changeCase(s,i): # change of the ith char in s
            diff=ord('a')-ord('A')
            if 'a'<=s[i]<='z': newChar= chr(ord(s[i])-diff)
            else: newChar= chr(ord(s[i])+diff)
            return s[:i]+newChar+s[i+1:]
        def backtrack(i,s):
            if i==n:
                res.append(s)
                return
            if isLetter(i):
                backtrack(i+1,changeCase(s,i)) # change case
            backtrack(i+1,s) # do not change case


        n=len(s)
        res=[]
        backtrack(0,s)
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted(['ab','Ab','aB','AB']), sorted(get_sol().letterCasePermutation('ab')))
    def test02(self):
        self.assertEqual(sorted(["a1b2","a1B2","A1b2","A1B2"]), sorted(get_sol().letterCasePermutation('a1b2')))
    def test03(self):
        self.assertEqual(sorted(["3z4","3Z4"]), sorted(get_sol().letterCasePermutation("3z4")))
    def test04(self):
        self.assertEqual(sorted(["12345"]), sorted(get_sol().letterCasePermutation("12345")))
    def test05(self):
        self.assertEqual(sorted(["0"]), sorted(get_sol().letterCasePermutation("0")))
    def test06(self):
        self.assertEqual(sorted(["00a","00A"]), sorted(get_sol().letterCasePermutation("00a")))
    def test07(self):
        self.assertEqual(sorted(["a00","A00"]), sorted(get_sol().letterCasePermutation("a00")))


from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[-1]=='(': return False
        if s[0]==')': return False
        bal = 0
        star=0
        for c in s:
            if bal<0 and star<abs(bal):
                return False
            if c=='(':
                bal+=1
            elif c==')':
                bal-=1
            else:
                star+=1
        if bal>0 and star<bal:
            return False

        bal=0
        star=0
        for c in s[::-1]:
            if bal>0 and star<abs(bal):
                return False
            if c=='(':
                bal+=1
            elif c==')':
                bal-=1
            else:
                star+=1
        if bal<0 and star<abs(bal):
            return False

        return True


class Correct:
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for c in s:
            if c in '(*':
                balance+=1
            else:
                balance-=1
            if balance<0: return False
        if balance==0: return True

        balance = 0
        for c in s[::-1]:
            if c in '*)':
                balance+=1
            else:
                balance-=1
            if balance<0: return False
        return True

class Tester(unittest.TestCase):
    def test02(self):
        a = "()"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test03(self):
        a = "(*)"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test04(self):
        a = "(*))"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test05(self):
        a = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test06(self):
        a = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test07(self):
        a = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test08(self):
        a = "**(*"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test09(self):
        a = "***((("
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test10(self):
        a = "(****("
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test11(self):
        a = "((**))(("
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test12(self):
        a = "**((*((**"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test13(self):
        a = "(((((*(((*(*******)))((*(((((****"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test14(self):
        a = "((*(((*(****))(("
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test15(self):
        a = "((*"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))
    def test16(self):
        a = "*))"
        self.assertEqual(Correct().checkValidString(a), Solution().checkValidString(a))

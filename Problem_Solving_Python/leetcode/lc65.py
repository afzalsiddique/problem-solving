import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    #define a DFA
    # https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
    def isNumber(self, s):
        state = [{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c in 'eE':
                c = 'e'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True
class Solution2:
    # wrong
    def isNumber(self, s: str) -> bool:
        digit_found = False
        sign_found=False
        digit_after_sign_found = False
        decimal_found = False
        digit_before_decimal_found = False
        digit_after_decimal_found = False
        e_found = False
        digit_after_e_found = False
        digit_before_e_found = False
        digit_before_sign_found = False
        for i in range(len(s)):
            if s[i] not in '-+0123456789eE.': return False
            if '0'<=s[i]<='9': digit_found = True

            if s[i]=='+' or s[i]=='-':
                if sign_found: return False
                sign_found = True
                digit_before_sign_found = digit_found
            if sign_found and '0'<=s[i]<='9':
                digit_after_sign_found=True

            if s[i]=='.':
                if decimal_found: return False
                decimal_found=True
                digit_before_decimal_found = digit_found
            if decimal_found and '0'<=s[i]<='9':
                digit_after_decimal_found = True

            if s[i]=='e' or s[i]=='E':
                if e_found: return False
                e_found=True
                digit_before_e_found = digit_found
            if e_found:
                if s[i]=='.': return False
                if '0'<=s[i]<='9':
                    digit_after_e_found=True

        if sign_found and digit_before_sign_found and digit_after_sign_found: return False
        if  (not e_found or (e_found and digit_before_e_found and digit_after_e_found))\
                and (not decimal_found or (decimal_found and digit_before_decimal_found) or (decimal_found and digit_after_decimal_found)):
            return True
        # if not(sign_found^digit_after_sign_found) \
        #         and not(e_found^digit_after_e_found) \
        #         and (not decimal_found or (decimal_found and digit_before_decimal_found) or (decimal_found and digit_after_decimal_found)):
        #     return True
        return False
class tester(unittest.TestCase):
    def test01(self):
        s = "0"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test02(self):
        s = "e"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test03(self):
        s = "."
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test04(self):
        s = ".1"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test05(self):
        s = "2"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test06(self):
        s = "0089"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test07(self):
        s = "-0.1"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test08(self):
        s = "+3.14"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test09(self):
        s = "4."
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test10(self):
        s = "-.9"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test11(self):
        s = "2e10"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test12(self):
        s = "-90E3"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test13(self):
        s = "3e7"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test14(self):
        s = "6e-1"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test15(self):
        s = "53.5e93"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test16(self):
        s = "6e-1"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test17(self):
        s = "-123.456e789"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test18(self):
        s = "abc"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test19(self):
        s = "1a"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test20(self):
        s = "1e"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test21(self):
        s = "e3"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test22(self):
        s = "99e2.5"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test23(self):
        s = "--6"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test24(self):
        s = "-+3"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test25(self):
        s = "95a54e53"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test26(self):
        s = "1+2"
        Output= False
        self.assertEqual(Output,get_sol().isNumber(s))
    def test27(self):
        s = "-5e-4"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))
    def test28(self):
        s = "1E9"
        Output= True
        self.assertEqual(Output,get_sol().isNumber(s))

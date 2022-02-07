from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/string-to-integer-atoi/discuss/4643/Java-Solution-with-4-steps-explanations/145893
    # only uses 32 bit variables
    def myAtoi(self, s: str) -> int:
        if len(s)==0:return 0
        INT_MAX,INT_MIN = 2147483647,-2147483648
        ans=0
        sign = 1
        for i in range(len(s)):
            if s[i]!=' ':break
        if s[i]=='+' or s[i]=='-':
            sign = -1 if s[i]=='-' else 1
            i+=1
        i_copy = i
        for i in range(i_copy,len(s)):
            if s[i]<'0' or s[i]>'9':break
            digit = int(s[i])
            tmp=(INT_MAX-digit)//10
            if ans > (INT_MAX-digit)//10:
                return INT_MAX if sign == 1 else INT_MIN
            ans = ans*10+digit
        return sign * ans
class Solution2:
    def myAtoi(self, s: str) -> int:
        M=2**31
        n=len(s)
        res=0
        i=0
        while i<n and s[i]==' ':
            i+=1
        sign=1
        if i<n and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and '0'<=s[i]<='9':
            res=res*10+ord(s[i])-ord('0')
            if res>M+1: break
            i+=1
        if sign==1:
            return min(res,M-1)
        return min(res,M)*sign


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(42,get_sol().myAtoi('42'))
    def test02(self):
        self.assertEqual(-42,get_sol().myAtoi('-42'))
    def test03(self):
        self.assertEqual(4193,get_sol().myAtoi("4193 with words"))
    def test04(self):
        self.assertEqual(0,get_sol().myAtoi("words and 987"))
    def test05(self):
        self.assertEqual(-2147483648,get_sol().myAtoi("-91283472332"))
    def test06(self):
        self.assertEqual(0,get_sol().myAtoi("+-12"))
    def test07(self):
        self.assertEqual(0,get_sol().myAtoi("00000-42a1234"))
    def test08(self):
        self.assertEqual(0,get_sol().myAtoi("   +0 123"))
    def test09(self):
        self.assertEqual(2147483646,get_sol().myAtoi("2147483646"))
    def test10(self):
        self.assertEqual(2147483647,get_sol().myAtoi("2147483647"))
    def test11(self):
        self.assertEqual(-2147483647,get_sol().myAtoi("-2147483647"))
    def test12(self):
        self.assertEqual(2147483647,get_sol().myAtoi("2147483648"))
    def test13(self):
        self.assertEqual(-2147483648,get_sol().myAtoi("-2147483648"))
    def test14(self):
        self.assertEqual(0,get_sol().myAtoi(""))
    def test15(self):
        self.assertEqual(0,get_sol().myAtoi(" "))
    def test16(self):
        self.assertEqual(1,get_sol().myAtoi("+1"))

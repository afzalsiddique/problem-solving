import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



# leetcode original
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop() # stack pop 1, sign
                res += stack.pop() # stack pop 2, operand
                operand = 0
        return res + sign * operand


class tester(unittest.TestCase):
    def test1(self):
        s = "1 + 1"
        Output= 2
        self.assertEqual(Output,Solution().calculate(s))
    def test2(self):
        s = " 2-1 + 2 "
        Output= 3
        self.assertEqual(Output,Solution().calculate(s))
    def test3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        Output= 23
        self.assertEqual(Output,Solution().calculate(s))
    def test4(self):
        s = " "
        Output= 0
        self.assertEqual(Output,Solution().calculate(s))
    def test5(self):
        s = "    "
        Output= 0
        self.assertEqual(Output,Solution().calculate(s))
    def test6(self):
        s = " 1"
        Output= 1
        self.assertEqual(Output,Solution().calculate(s))
    def test7(self):
        s = "- (3 + (4 + 5))"
        Output= -12
        self.assertEqual(Output,Solution().calculate(s))
    def test8(self):
        s = "2147483647"
        Output= 2147483647
        self.assertEqual(Output,Solution().calculate(s))
    def test9(self):
        s = "11 + 11"
        Output= 22
        self.assertEqual(Output,Solution().calculate(s))

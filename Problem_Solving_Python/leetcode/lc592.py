import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103384/Small-simple-C%2B%2BJavaPython
    def fractionAddition(self, expression):
        ints = expression.replace('+', ' +').replace('-', ' -')
        # print(ints)
        ints = ints.split()
        ints = list(map(str,ints))
        # print(ints)
        A, B = 0, 1
        for x in ints:
            a,b = map(int,x.split('/'))
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return "{}/{}".format(A,B)

class tester(unittest.TestCase):
    def test_1(self):
        expression = "-1/2+1/2"
        Output= "0/1"
        self.assertEqual(Output,get_sol().fractionAddition(expression))
    def test_2(self):
        expression = "-1/2+1/2+1/3"
        Output= "1/3"
        self.assertEqual(Output,get_sol().fractionAddition(expression))
    def test_3(self):
        expression = "1/3-1/2"
        Output= "-1/6"
        self.assertEqual(Output,get_sol().fractionAddition(expression))
    def test_4(self):
        expression = "5/3+1/3"
        Output= "2/1"
        self.assertEqual(Output,get_sol().fractionAddition(expression))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
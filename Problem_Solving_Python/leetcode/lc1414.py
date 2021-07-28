import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove
    def findMinFibonacciNumbers(self, k):
        def h(k):
            if k < 2: return k
            a, b = 1, 1
            while b <= k:
                a, b = b, a+b
            return 1+h(k-a)

        return h(k)

class tester(unittest.TestCase):
    def test_1(self):
        k = 7
        Output= 2
        self.assertEqual(Output,get_sol().findMinFibonacciNumbers(k))
    def test_2(self):
        k = 10
        Output= 2
        self.assertEqual(Output,get_sol().findMinFibonacciNumbers(k))
    def test_3(self):
        k = 19
        Output= 3
        self.assertEqual(Output,get_sol().findMinFibonacciNumbers(k))
    def test_4(self):
        k = 10**9
        Output= 14
        self.assertEqual(Output,get_sol().findMinFibonacciNumbers(k))
    # def test_5(self):
    # def test_6(self):
import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390319/How-to-reach-the-optimal-solution-or-Explained-with-Intuition-and-Diagram
    def minSwaps(self, s: str) -> int:
        stack_size=0
        imbalance = 0
        for i in range(len(s)):
            ch=s[i]
            if ch == '[':
                stack_size+=1
            else:  # ']'
                if stack_size: # balanced ] found
                    stack_size-=1
                else: # imbalanced ] found
                    imbalance+=1
        return (imbalance + 1) // 2

class Tester(unittest.TestCase):
    def test_1(self):
        s = "][]["
        Output= 1
        self.assertEqual(Output,get_sol().minSwaps(s))
    def test_2(self):
        s = "]]][[["
        Output= 2
        self.assertEqual(Output,get_sol().minSwaps(s))
    def test_3(self):
        s = "[]"
        Output= 0
        self.assertEqual(Output,get_sol().minSwaps(s))
    def test_4(self):
        s = "]]][]]][[[[["
        Output= 3
        self.assertEqual(Output,get_sol().minSwaps(s))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

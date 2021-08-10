import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        res = []
        cnt = 0
        for c in s:
            if c=='(':
                cnt += 1
                res.append(cnt % 2)  # group determined through parity (odd/even?) of depth
            else:
                cnt -=1
                res.append(1^(cnt % 2))  # group determined through parity (odd/even?) of depth
        return res
class Solution2:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        res = []
        cnt = 0
        for c in s:
            if c=='(':
                cnt += 1
                res.append(cnt % 2)  # group determined through parity (odd/even?) of depth
            else:
                res.append(cnt % 2)  # group determined through parity (odd/even?) of depth
                cnt -=1

        return res




class Tester(unittest.TestCase):
    def test_1(self):
        seq = "(()())"
        Output= [1, 0, 0, 0, 0, 1]
        self.assertEqual(Output,get_sol().maxDepthAfterSplit(seq))
    def test_2(self):
        seq = "()(())()"
        Output= [1, 1, 1, 0, 0, 1, 1, 1]
        self.assertEqual(Output,get_sol().maxDepthAfterSplit(seq))
    def test_3(self):
        seq = "(((()))((())))"
        Output= [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
        self.assertEqual(Output,get_sol().maxDepthAfterSplit(seq))
    def test_4(self):
        seq = "((()(()((()()))((()()((()(()(()())(()(()))))))))))"
        Output= [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(Output,get_sol().maxDepthAfterSplit(seq))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
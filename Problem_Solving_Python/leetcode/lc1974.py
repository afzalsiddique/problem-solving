from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer='a'
        total=0
        for c in word:
            option1=(ord(c)-ord(pointer))%26
            option2=(ord(pointer)-ord(c))%26
            pointer=c
            minn=min(option1,option2)
            total+=minn
        return total+len(word)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        word = "abc"
        Output= 5
        self.assertEqual(Output, get_sol().minTimeToType(word))
    def test_2(self):
        word = "bza"
        Output= 7
        self.assertEqual(Output, get_sol().minTimeToType(word))
    def test_3(self):
        word = "zjpc"
        Output= 34
        self.assertEqual(Output, get_sol().minTimeToType(word))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

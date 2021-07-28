import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def minFlips(self, target: str) -> int:
        cnt=0
        for i in range(len(target)):
            x=int(target[i]) # all bulbs after ith bulb has been flipped cnt times
            if (x+cnt)%2:
                cnt+=1
        return cnt

class MyTestCase(unittest.TestCase):
    def test_1(self):
        target = "10111"
        Output= 3
        self.assertEqual(Output,get_sol().minFlips(target))
    def test_2(self):
        target = "101"
        Output= 3
        self.assertEqual(Output,get_sol().minFlips(target))
    def test_3(self):
        target = "00000"
        Output= 0
        self.assertEqual(Output,get_sol().minFlips(target))
    def test_4(self):
        target = "001011101"
        Output= 5
        self.assertEqual(Output,get_sol().minFlips(target))
    # def test_5(self):
    # def test_6(self):
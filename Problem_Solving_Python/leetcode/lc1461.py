import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        sett=set()
        for i in range(n-k+1):
            sett.add(s[i:i+k])
        if len(sett)==2**k:
            return True
        return False
        # for i in range(2**k):
        #     binary = bin(i)[2:]
        #     if len(binary)<k:
        #         binary='0'*(k-len(binary)) + binary


class tester(unittest.TestCase):
    def test01(self):
        s = "00110110"
        k = 2
        Output= True
        self.assertEqual(Output,get_sol().hasAllCodes(s,k))
    def test02(self):
        s = "00110"
        k = 2
        Output= True
        self.assertEqual(Output,get_sol().hasAllCodes(s,k))
    def test03(self):
        s = "0110"
        k = 1
        Output= True
        self.assertEqual(Output,get_sol().hasAllCodes(s,k))
    def test04(self):
        s = "0110"
        k = 2
        Output= False
        self.assertEqual(Output,get_sol().hasAllCodes(s,k))
    def test05(self):
        s = "0000000001011100"
        k = 4
        Output= False
        self.assertEqual(Output,get_sol().hasAllCodes(s,k))

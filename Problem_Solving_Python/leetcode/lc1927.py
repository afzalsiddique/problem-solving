import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/sum-game/discuss/1328950/Simple-Python-Solution%3A-Simplify-Problem-O(n)
    def sumGame(self, num: str) -> bool:
        # count how many question marks and what sums we have on both sides
        sumLeft, sumRight = 0, 0
        qmLeft, qmRight = 0, 0
        for i in range(len(num)):
            if i < len(num)//2:
                if num[i] == "?": qmLeft += 1
                else: sumLeft += int(num[i])
            else:
                if num[i] == "?": qmRight += 1
                else: sumRight += int(num[i])

        remainingQM = abs(qmLeft-qmRight)
        remainingSum = abs(sumRight-sumLeft)

        # simplify the problem: e.g. ????5.123?? can be simplified to  ??5.123
        # -> remove quesiton marks that appear on both sides. because alice plays first and replaces a QM with any number,
        # and bob plays afterwards and tries to get the same sum, he can pick a QM on the other side and just put in the
        # same number as alice.

        # also take the difference of the numbers: ??5.123  means we have 2 question marks that should result in the
        # number 3 (1+2+3 - 5)

        if (math.ceil(remainingQM/2))*9>remainingSum: return True # QMs that alice can set.
        if (remainingQM//2)*9 < remainingSum: return True # question marks that bob can set

        return False



class tester(unittest.TestCase):
    def test_1(self):
        num = "5023"
        Output= False
        self.assertEqual(Output,get_sol().sumGame(num))
    def test_2(self):
        num = "25??"
        Output= True
        self.assertEqual(Output,get_sol().sumGame(num))
    def test_3(self):
        num = "?3295???"
        Output= False
        self.assertEqual(Output,get_sol().sumGame(num))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):

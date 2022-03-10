from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        res=[[] for _ in range(numRows)]
        index, step = 0, 1

        for x in s:
            res[index].append(x)
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            index += step

        # print(res)
        res=list(map(''.join,res))
        # print(res)
        res=''.join(res)
        # print(res)
        return res


class Solution2:
    def get_range(self,numRows,n):
        res=[]
        n_copy=n
        while n>0:
            for i in range(numRows):
                res.append(i)
            for i in reversed(range(1,numRows-1)):
                res.append(i)
            n = n - (numRows + (numRows-2))
        return res[:n_copy]
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        res=[[] for _ in range(numRows)]
        my_range = self.get_range(numRows,len(s))
        for i in range(len(s)):
            res[my_range[i]].append(s[i])
        # print(res)
        res=list(map(''.join,res))
        # print(res)
        res=''.join(res)
        # print(res)
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual("PAHNAPLSIIGYIR",get_sol().convert("PAYPALISHIRING", 3))
    def test02(self):
        self.assertEqual("PINALSIGYAHRPI",get_sol().convert("PAYPALISHIRING", 4))
    def test03(self):
        self.assertEqual("A",get_sol().convert("A", 1))
    def test04(self):
        self.assertEqual("ABC",get_sol().convert("ABC", 1))

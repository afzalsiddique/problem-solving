import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution(object):
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

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("PAHNAPLSIIGYIR",Solution().convert(s = "PAYPALISHIRING", numRows = 3))
    def test2(self):
        self.assertEqual("PINALSIGYAHRPI",Solution().convert(s = "PAYPALISHIRING", numRows = 4))
    def test3(self):
        self.assertEqual("A",Solution().convert(s = "A", numRows = 1))

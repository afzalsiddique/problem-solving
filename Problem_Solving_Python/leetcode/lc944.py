import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m,n=len(strs),len(strs[0])
        res=0
        for j in range(n):
            flag=False
            for i in range(1,m):
                if strs[i][j]<strs[i-1][j]:
                    flag=True
                    break
            if flag:
                res+=1
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().minDeletionSize(["cba","daf","ghi"]))
    def test02(self):
        self.assertEqual(0, get_sol().minDeletionSize(["a","b"]))
    def test03(self):
        self.assertEqual(3, get_sol().minDeletionSize(["zyx","wvu","tsr"]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):

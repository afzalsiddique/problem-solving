import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # longest increasing subsequence
    def minDeletionSize(self, A: List[str]) -> int:
        m,n=len(A),len(A[0])
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                flag=True
                for k in range(m):
                    if A[k][i]<A[k][j]:
                        flag=False
                        break
                if flag:
                    dp[i]=max(dp[i],dp[j]+1)
        return n-max(dp)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().minDeletionSize(["babca","bbazb"]))
    def test02(self):
        self.assertEqual(4, get_sol().minDeletionSize(["edcba"]))
    def test03(self):
        self.assertEqual(0, get_sol().minDeletionSize(["ghi","def","abc"]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):

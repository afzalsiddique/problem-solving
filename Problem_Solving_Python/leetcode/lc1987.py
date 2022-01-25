from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def numberOfUniqueGoodSubsequences(self, s: str) -> int:
        M=10**9+7
        n=len(s)
        dp=[0]*2
        dp[ord(s[0])-ord('0')]=1
        for i in range(1,n):
            tmp=sum(x for x in dp)
            idx=ord(s[i])-ord('0')
            if dp[0]!=0:
                dp[idx]=tmp
            else:
                dp[idx]=tmp+1
            dp[idx]%=M
        return sum(dp)%M

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().numberOfUniqueGoodSubsequences("001"))
    def test2(self):
        self.assertEqual(2, get_sol().numberOfUniqueGoodSubsequences("11"))
    def test3(self):
        self.assertEqual(5, get_sol().numberOfUniqueGoodSubsequences("101"))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

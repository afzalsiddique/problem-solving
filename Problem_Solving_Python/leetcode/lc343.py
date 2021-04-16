import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    def integerBreak(self, n: int) -> int:
        di={}
        def helper(n):
            if n==1 or n==2: return 1
            if n==3: return 2
            if n in di: return di[n]
            result=0
            for i in range(2,n):
                a=i
                b=n-a
                if a>b:break
                result=max(result,a*helper(b),a*b)
            di[n]=result
            return di[n]

        return helper(n)

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,Solution().integerBreak(1))
    def test2(self):
        self.assertEqual(1,Solution().integerBreak(2))
    def test3(self):
        self.assertEqual(2,Solution().integerBreak(3))
    def test4(self):
        self.assertEqual(4,Solution().integerBreak(4))
    def test5(self):
        self.assertEqual(6,Solution().integerBreak(5))
    def test6(self):
        self.assertEqual(9,Solution().integerBreak(6))
    def test7(self):
        self.assertEqual(36,Solution().integerBreak(10))
    def test8(self):
        self.assertEqual(18,Solution().integerBreak(8))

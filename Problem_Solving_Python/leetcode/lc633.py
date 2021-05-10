import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()



class Solution:
    # leetcode original solution 4
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(lo, hi, key):
            while lo<=hi:
                mid=(lo+hi)//2
                temp=mid*mid
                if temp == key:
                    return True
                if key<temp:
                    hi=mid-1
                else:
                    lo=mid+1
            return False
        for a in range(int(math.sqrt(c))+1):
            b = c-a*a
            if binary_search(0,b,b): return True
        return False


class tester(unittest.TestCase):
    def test1(self):
        c = 1
        Output= True
        self.assertEqual(Output,Solution().judgeSquareSum(c))
    def test2(self):
        c = 5
        Output= True
        self.assertEqual(Output,Solution().judgeSquareSum(c))
    def test3(self):
        c = 3
        Output= False
        self.assertEqual(Output,Solution().judgeSquareSum(c))
    def test4(self):
        c = 4
        Output= True
        self.assertEqual(Output,Solution().judgeSquareSum(c))
    def test5(self):
        c = 2
        Output= True
        self.assertEqual(Output,Solution().judgeSquareSum(c))
    def test6(self):
        c = 999999999
        Output= False
        self.assertEqual(Output,Solution().judgeSquareSum(c))

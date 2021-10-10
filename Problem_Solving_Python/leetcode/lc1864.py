import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        count = Counter(s)
        if abs(count['0']-count['1'])>1: return -1
        if count['0']<count['1']: # make all '0's  equal to '1's and all '1's equal to '0's
            tmp = map(lambda x: '0' if x=='1' else '1', s)
            return self.minSwaps(''.join(tmp))

        count_odd_indices = 0
        for i in range(n): # count number of odd indices of zero
            if s[i]=='0':
                count_odd_indices+=i%2

        count_even_indices = count['0']-count_odd_indices

        if n%2==0:
            return min(count_even_indices,count_odd_indices)
        return count_odd_indices



class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "111000"
        Output= 1
        self.assertEqual(Output, get_sol().minSwaps(s))
    def test2(self):
        s = "010"
        Output= 0
        self.assertEqual(Output, get_sol().minSwaps(s))
    def test3(self):
        s = "1110"
        Output= -1
        self.assertEqual(Output, get_sol().minSwaps(s))
    def test4(self):
        s = "1001"
        Output= 1
        self.assertEqual(Output, get_sol().minSwaps(s))
    def test5(self):
        s = "100"
        Output= 1
        self.assertEqual(Output, get_sol().minSwaps(s))
    def test6(self):
        s = "010110"
        Output= 1
        self.assertEqual(Output, get_sol().minSwaps(s))
    # def test7(self):

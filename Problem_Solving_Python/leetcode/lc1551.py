import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2*i+1 for i in range(n)]
        cnt = 0
        for i in range(n//2):
            if n%2:
                cnt+=arr[n//2]-arr[i]
            else:
                cnt+=n-arr[i]
        return cnt


class tester(unittest.TestCase):
    def test_01(self):
        n = 3
        Output= 2
        self.assertEqual(Output,get_sol().minOperations(n))
    def test_02(self):
        n = 5
        Output= 6
        self.assertEqual(Output,get_sol().minOperations(n))
    def test_03(self):
        n = 7
        Output= 12
        self.assertEqual(Output,get_sol().minOperations(n))
    def test_04(self):
        n = 9
        Output= 20
        self.assertEqual(Output,get_sol().minOperations(n))
    def test_05(self):
        n = 6
        Output= 9
        self.assertEqual(Output,get_sol().minOperations(n))
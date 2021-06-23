import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def numFriendRequests(self, ages):
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a)
        c = Counter(ages)
        cnt=0
        for a in c:
            for b in c:
                if request(a,b):
                    if a==b:
                        cnt+=c[a]*(c[b]-1)
                    else:
                        cnt+=c[a]*c[b]
        return cnt


class tester(unittest.TestCase):
    def test_01(self):
        Input= [16,16]
        Output= 2
        self.assertEqual(Output,get_sol().numFriendRequests(Input))
    def test_02(self):
        Input= [16,17,18]
        Output= 2
        self.assertEqual(Output,get_sol().numFriendRequests(Input))
    def test_03(self):
        Input= [20,30,100,110,120]
        Output= 3
        self.assertEqual(Output,get_sol().numFriendRequests(Input))

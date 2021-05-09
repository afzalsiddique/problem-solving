import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    # bucket sort
    def customSortString(self, S: str, T: str) -> str:
        di={c:i for i,c in enumerate(S)}
        buckets=[[] for _ in range(len(S)+1)]
        for i,c in enumerate(T):
            if c in di:
                buckets[di[c]].append(c)
            else:
                buckets[-1].append(c)
        # convert to string
        buckets=list(map(''.join,buckets))
        buckets=''.join(buckets)
        return buckets


class tester(unittest.TestCase):
    def test01(self):
        S = "cba"
        T = "abcd"
        Output= "cbad"
        self.assertEqual(Output,get_sol().customSortString(S,T))
    def test02(self):
        S = "cba"
        T = "abdc"
        Output= "cbad"
        self.assertEqual(Output,get_sol().customSortString(S,T))
    def test03(self):
        S = "kqep"
        T = "pekeq"
        Output= "kqeep"
        self.assertEqual(Output,get_sol().customSortString(S,T))


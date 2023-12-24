from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(x): return Solution2(x)

# https://www.youtube.com/watch?v=fWS0TCcr-lE

class Solution:
    # w      : [1,4, 5]
    # cum_sum: [1,5,10]
    # [0],[1,2,3,4],[5,6,7,8,9]
    # bisect_right
    def __init__(self, w: List[int]):
        self.pre_sum=list(accumulate(w))
    def pickIndex(self) -> int:
        maxx=self.pre_sum[-1]
        rand_int=random.randint(0,maxx-1)
        randIdx=bisect_right(self.pre_sum, rand_int)
        return randIdx
class Solution2:
    # bisect_left
    def __init__(self, w: List[int]):
        self.pre_sum=list(accumulate(w))
    def pickIndex(self) -> int:
        maxx=self.pre_sum[-1]
        rand_int = random.randint(1, maxx)
        randIdx = bisect_left(self.pre_sum, rand_int)
        return randIdx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution([1,3,6])
        di = {}
        for _ in range(10000):
            idx = sol.pickIndex()
            if idx in di:
                di[idx]+=1
            else:
                di[idx]=1
        print(di)
        expected = {0:1000,1:3000,2:6000}
        actual = di
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution([1])
        di = {}
        for _ in range(10000):
            idx = sol.pickIndex()
            if idx in di:
                di[idx]+=1
            else:
                di[idx]=1
        print(di)
        expected = {0:10000}
        actual = di
        self.assertEqual(expected, actual)


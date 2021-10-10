import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        mn_heap = []
        for x in nums:
            if len(mn_heap)<k:
                heappush(mn_heap,int(x))
            else:
                tmp = heappop(mn_heap)
                heappush(mn_heap,max(tmp,int(x)))
        return str(min(mn_heap))


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k = ["3","6","7","10"],  4
        Output= "3"
        self.assertEqual(Output, get_sol().kthLargestNumber(nums,k))
    def test2(self):
        nums,k = ["2","21","12","1"],  3
        Output= "2"
        self.assertEqual(Output, get_sol().kthLargestNumber(nums,k))
    def test3(self):
        nums,k = ["0","0"],  2
        Output= "0"
        self.assertEqual(Output, get_sol().kthLargestNumber(nums,k))
    def test4(self):
        nums,k = ["1","2","2"],  3
        Output= "1"
        self.assertEqual(Output, get_sol().kthLargestNumber(nums,k))
    # def test5(self):
    # def test6(self):

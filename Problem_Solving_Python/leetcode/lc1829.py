import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        maxx=(1<<maximumBit)-1 # 2**maximumBit -1
        pre_xor = list(itertools.accumulate(nums,lambda a,b: a^b))
        li = [maxx^pre_xor[i] for i in range(n)]
        li.reverse()
        return li


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,maximumBit = [0,1,1,3],  2
        Output= [0,3,2,3]
        self.assertEqual(Output, get_sol().getMaximumXor(nums,maximumBit))
    def test2(self):
        nums,maximumBit = [2,3,4,7],  3
        Output= [5,2,6,5]
        self.assertEqual(Output, get_sol().getMaximumXor(nums,maximumBit))
    def test3(self):
        nums,maximumBit = [0,1,2,2,5,7],  3
        Output= [4,3,6,4,6,7]
        self.assertEqual(Output, get_sol().getMaximumXor(nums,maximumBit))
    # def test4(self):
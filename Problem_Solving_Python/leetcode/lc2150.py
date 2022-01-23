from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        def removeNeighbors(x):
            if x not in freq:
                return

            xLeft=x-1
            while xLeft in freq:
                freq.pop(xLeft)
                xLeft-=1

            xRight=x+1
            while xRight in freq:
                freq.pop(xRight)
                xRight+=1

            if freq[x]>1:
                freq[x]=0

            if xLeft!=x-1 or xRight!=x+1:
                freq[x]=0

            if freq[x]==0:
                freq.pop(x)

        freq=Counter(nums)
        for x in nums:
            removeNeighbors(x)
        return list(freq.keys())

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([10,8],get_sol().findLonely([10,6,5,8]))
    def test02(self):
        self.assertEqual([1,5],get_sol().findLonely([1,3,5,3]))
    def test03(self):
        self.assertEqual([1],get_sol().findLonely([1]))
    def test04(self):
        self.assertEqual([],get_sol().findLonely([1,1,1,1]))
    def test05(self):
        self.assertEqual([],get_sol().findLonely([1,1,3,3]))

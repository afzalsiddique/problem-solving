from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        i,j=0,0
        while i<n and j<n:
            while j<n and nums[j]<0:
                j+=1

            if j<n:
                res[i]=nums[j]

            j+=1
            i+=2

        i,j=1,0
        while i<n and j<n:
            while j<n and nums[j]>0:
                j+=1

            if j<n:
                res[i]=nums[j]

            j+=1
            i+=2
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,-2,1,-5,2,-4],get_sol().rearrangeArray([3,1,-2,-5,2,-4]))
    def test02(self):
        self.assertEqual([1,-1],get_sol().rearrangeArray([-1,1]))
    def test03(self):
        self.assertEqual([1,-1],get_sol().rearrangeArray([1,-1]))
    # def test04(self):
    # def test05(self):

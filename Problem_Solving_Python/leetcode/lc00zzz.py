import itertools;from itertools import accumulate; from math import floor,ceil,sqrt,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        zeros=sum(1 for x in nums if x==0)
        if zeros>=2: return [0]*n
        if zeros==1:
            prod=1
            idx_zero=-1
            for i,x in enumerate(nums):
                if x==0:
                    idx_zero=i
                else:
                    prod*=x
            return [0]*idx_zero+[prod]+[0]*(n-1-idx_zero)
        prod=reduce(lambda a,b:a*b,nums)
        return [prod//x for x in nums]


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([60, 40, 30, 24], get_sol().productExceptSelf([2,3,4,5]))
    def test02(self):
        self.assertEqual([24,12,8,6], get_sol().productExceptSelf([1,2,3,4]))
    def test03(self):
        self.assertEqual([0,0,9,0,0], get_sol().productExceptSelf([-1,1,0,-3,3]))
    def test04(self):
        self.assertEqual([0,0,0,0,0], get_sol().productExceptSelf([1,0,2,3,0]))

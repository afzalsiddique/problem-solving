from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def getSign(nums):
            if all(x>0 for x in nums): return 1
            if all(x<0 for x in nums): return -1
            return 0
        @cache
        def dp(i,j):
            if i==m or j==n: return 0
            return max(
                nums1[i]*nums2[j]+dp(i+1,j+1),
                dp(i+1,j),
                dp(i,j+1))

        m,n=len(nums1),len(nums2)
        pairMax=max(nums1[i]*nums2[j] for i in range(m) for j in range(n))
        res=dp(0,0)
        sign1,sign2=getSign(nums1),getSign(nums2)
        if sign1*sign2==-1: # all pos in one array and all neg in the other array
            return pairMax
        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(18,get_sol().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))
    def test02(self):
        self.assertEqual(21,get_sol().maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7]))
    def test03(self):
        self.assertEqual(-1,get_sol().maxDotProduct(nums1 = [-1,-1], nums2 = [1,1]))
    def test04(self):
        self.assertEqual(50,get_sol().maxDotProduct([-5,3,-5,-3,1], [-2,4,2,5,-5]))
    def test05(self):
        self.assertEqual(72,get_sol().maxDotProduct([-3,-8,3], [7,-9]))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):

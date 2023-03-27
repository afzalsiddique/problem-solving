from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        @cache
        def dp(i,j,k):
            if k==1:
                tmp1=nums1[i:]
                tmp2=nums2[j:]
                one=max(tmp1) if tmp1 else float('-inf')
                two=max(tmp2) if tmp2 else float('-inf')
                return max(one,two)
            if i==len(nums1) or j==len(nums2): return float('-inf')
            part1=dp(i+1,j,k-1)
            ans1=nums1[i]*10**(k-1)+dp(i+1,j,k-1)
            part2=dp(i,j+1,k-1)
            ans2=nums2[j]*10**(k-1)+dp(i,j+1,k-1)
            ans3=dp(i+1,j,k)
            ans4=dp(i,j+1,k)
            return max(ans1,ans2,ans3,ans4)

        return [int(c) for c in str(dp(0,0,k))]


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums1,nums2,k = [3,4,6,5],  [9,1,2,5,8,3],  5
        Output= [9,8,6,5,3]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test2(self):
        nums1,nums2,k = [6,7],  [6,0,4],  5
        Output= [6,7,6,0,4]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test3(self):
        nums1,nums2,k = [3,9],  [8,9],  3
        Output= [9,8,9]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test4(self):
        nums1,nums2,k = [8,6,9], [1,7,5], 3
        Output= [9,7,5]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test5(self):
        nums1,nums2,k = [6,9], [7,5], 2
        Output= [9,7]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    # def test6(self):
    # def test7(self):
    # def test8(self):

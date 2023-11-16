from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        right=nums[-1]
        for i in range(n-2,-1,-1):
            noOfParts=ceil(nums[i]/right) # nums[i] will be divided into noOfParts
            right=nums[i]//noOfParts # the smallest value after dividing
            res+=noOfParts-1 # dividing into noOfParts will require (noOfParts-1) steps
        return res





class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().minimumReplacement([3,9,3]))
    def test2(self):
        self.assertEqual(0, get_sol().minimumReplacement([1,2,3,4,5]))
    def test3(self):
        self.assertEqual(4, get_sol().minimumReplacement([3,10,3]))
    def test4(self):
        self.assertEqual(8, get_sol().minimumReplacement([3,10,10,3]))
    def test5(self):
        self.assertEqual(15, get_sol().minimumReplacement([16,1,11,23]))
    def test6(self):
        self.assertEqual(48, get_sol().minimumReplacement([24,11,16,1,11,23])) # 48=23+10+15
    def test7(self):
        self.assertEqual(73, get_sol().minimumReplacement([19,7,2,24,11,16,1,11,23]))
    def test8(self):
        self.assertEqual(6, get_sol().minimumReplacement([12,9,7,6]))
    def test9(self):
        self.assertEqual(6, get_sol().minimumReplacement([12,9,7,6,17,19,21]))

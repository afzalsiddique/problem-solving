from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=Dd-yJylrcOY&pp
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        freq=defaultdict(int)
        res=float('inf')
        right_idx=0
        for i in range(n):
            start=nums[i]
            right_end=start+n-1
            while right_idx<n and nums[right_idx]<=right_end:
                freq[nums[right_idx]]+=1
                right_idx+=1
            res=min(res,n-len(freq))
            freq[nums[i]]-=1
            if freq[nums[i]]==0:
                freq.pop(nums[i])
        return res





class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().minOperations([4,2,5,3]))
    def test02(self):
        self.assertEqual(1, get_sol().minOperations([1,2,3,5,6]))
    def test03(self):
        self.assertEqual(3, get_sol().minOperations([1,10,100,1000]))
    def test04(self):
        self.assertEqual(2, get_sol().minOperations([8,5,9,9,8,4]))
    def test05(self):
        self.assertEqual(1, get_sol().minOperations([18, 24, 26]))
    def test06(self):
        self.assertEqual(2, get_sol().minOperations([18, 24, 26, 28]))
    def test07(self):
        self.assertEqual(5, get_sol().minOperations([41,33,29,33,35,26,47,24,18,28]))
    # def test08(self):
    def testDummy1(self):
        self.assertEqual(2, get_sol().minOperations([4,5,8,8,9,9]))
    # def testDummy2(self):
    #     self.assertEqual(2, get_sol().minOperations([41,33,29,33,35,26,47,24,18,28]))

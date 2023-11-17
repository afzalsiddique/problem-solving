from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=wDROrQwyZjQ
    def numOfWays(self, nums: List[int]) -> int:
        M=10**9+7
        @cache
        def factorial(x): return 1 if x in [0,1] else x*factorial(x-1)
        def ncr(n,r): return factorial(n)//(factorial(r)*factorial(n-r))
        def count(li:List[int]):
            if len(li)<=2: return 1
            root_val=li[0]
            left=[x for x in li[1:] if x<root_val]
            right=[x for x in li[1:] if x>root_val]
            n=len(li)-1
            return ncr(n,len(left))*count(left)*count(right)

        return (count(nums)-1)%M


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().numOfWays([2,1,3]))
    def test02(self):
        self.assertEqual(5,get_sol().numOfWays([3,4,5,1,2]))
    def test03(self):
        self.assertEqual(0,get_sol().numOfWays([1,2,3]))
    def test04(self):
        self.assertEqual(216212978,get_sol().numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))
    # def test05(self):
    # def test06(self):

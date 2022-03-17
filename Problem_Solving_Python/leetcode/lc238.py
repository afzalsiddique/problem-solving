from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space/67603
    def productExceptSelf(self, A: List[int]) -> List[int]:
        n=len(A)
        res=[1]*n
        left=1
        for i in range(n-1):
            left*=A[i]
            res[i+1]=left

        right=1
        for i in range(n-1,0,-1):
            right*=A[i]
            res[i-1]*=right
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([60, 40, 30, 24], get_sol().productExceptSelf([2,3,4,5]))


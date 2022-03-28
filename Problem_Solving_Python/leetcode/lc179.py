from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(n1:str,n2:str):
            return int(n2+n1)-int(n1+n2)
        if any(nums)==False: # if all zeros
        # if any(x!=0 for x in nums)==False:
        # if all(x==0 for x in nums):
            return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        if any(nums)==False:
            return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0))))

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual("9534330",get_sol().largestNumber([3,30,34,5,9]))
    def test02(self):
        self.assertEqual("0",get_sol().largestNumber([0,0]))
    def test03(self):
        self.assertEqual("10",get_sol().largestNumber([0,1]))

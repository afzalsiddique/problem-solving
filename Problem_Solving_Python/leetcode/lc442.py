from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                res.append(idx+1)
            else:
                nums[idx]=abs(nums[idx])*(-1)
        return res
class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,3],get_sol().findDuplicates([4,3,2,7,8,2,3,1]))
    def test02(self):
        self.assertEqual([1],get_sol().findDuplicates([1,1,2]))
    def test03(self):
        self.assertEqual([],get_sol().findDuplicates([1]))

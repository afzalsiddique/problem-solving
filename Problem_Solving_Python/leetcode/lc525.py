from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # time O(n) space O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        maxx=0
        summ=0
        di={0:-1}
        for i,num in enumerate(nums):
            if num==1: summ+=1
            else: summ-=1
            if summ not in di:
                di[summ]=i
            else:
                maxx=max(maxx,i-di[summ])
        return maxx


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().findMaxLength([1,0]))
    def test02(self):
        self.assertEqual(2,get_sol().findMaxLength([0,1,0]))
    def test03(self):
        self.assertEqual(6,get_sol().findMaxLength([0,0,1,0,0,0,1,1]))

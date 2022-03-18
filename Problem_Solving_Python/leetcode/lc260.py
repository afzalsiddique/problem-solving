from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=L-EaPf5tD5A
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2: return nums
        xy=0
        for num in nums:
            xy=xy^num
        res=[0,0]
        last_set_bit = xy & (-xy)
        for num in nums:
            if last_set_bit & num:
                res[0]=res[0] ^ num
            else:
                res[1]=res[1] ^ num
        return res



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted([3,5]),sorted(get_sol().singleNumber([1,2,1,3,2,5])))
    def test02(self):
        self.assertEqual(sorted([-1,0]),sorted(get_sol().singleNumber([-1,0])))
    def test03(self):
        self.assertEqual(sorted([0,1]),sorted(get_sol().singleNumber([0,1])))

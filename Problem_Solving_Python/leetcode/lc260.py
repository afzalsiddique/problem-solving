from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=L-EaPf5tD5A
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2: return nums
        x_xor_y=0
        for num in nums:
            x_xor_y=x_xor_y^num
        res=[0,0]
        last_set_bit = x_xor_y & (-x_xor_y)
        for num in nums:
            if last_set_bit & num:
                res[0]=res[0] ^ num
            else:
                res[1]=res[1] ^ num
        return res

class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def isOn(mask,i): return (mask>>i)&1
        x_xor_y=reduce(lambda a,b:a^b, nums)
        last_set_bit = int(log2(x_xor_y & (-x_xor_y)))
        x,y=0,0
        for num in nums:
            if isOn(num,last_set_bit):
                x^=num
            else:
                y^=num
        return [x,y]

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted([3,5]),sorted(get_sol().singleNumber([1,2,1,3,2,5])))
    def test02(self):
        self.assertEqual(sorted([-1,0]),sorted(get_sol().singleNumber([-1,0])))
    def test03(self):
        self.assertEqual(sorted([0,1]),sorted(get_sol().singleNumber([0,1])))

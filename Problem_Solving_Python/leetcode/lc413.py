from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=IShCyNmsoL8
    total=0
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def helper():
            if len(nums)<3: return 0
            if nums[-1]-nums[-2]==nums[-2]-nums[-3]:
                ans=1
                nums.pop()
                ans+=helper()
                self.total+=ans
                return ans
            else:
                nums.pop()
                helper()
                return 0

        helper()
        return self.total

# class Solution2:
    # for tabulation see the link below:
    # https://leetcode.com/problems/arithmetic-slices/discuss/90093/3ms-C%2B%2B-Standard-DP-Solution-with-Very-Detailed-Explanation

class Tester(unittest.TestCase):
    def test1(self):
        nums = [1,2,3,4]
        Output= 3
        self.assertEqual(Output,get_sol().numberOfArithmeticSlices(nums))
    def test2(self):
        nums = [1]
        Output= 0
        self.assertEqual(Output,get_sol().numberOfArithmeticSlices(nums))
    def test3(self):
        nums = [1,2,3,4,5]
        Output= 6
        self.assertEqual(Output,get_sol().numberOfArithmeticSlices(nums))
    def test4(self):
        nums = [1,2,3,8,9,10]
        Output= 2
        self.assertEqual(Output,get_sol().numberOfArithmeticSlices(nums))


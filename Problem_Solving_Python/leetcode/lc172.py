from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        return n//5+self.trailingZeroes(n//5)



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().trailingZeroes(5))
    def test02(self):
        self.assertEqual(0,get_sol().trailingZeroes(0))

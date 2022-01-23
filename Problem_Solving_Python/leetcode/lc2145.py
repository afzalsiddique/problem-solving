from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pre=[0]+list(accumulate(differences))
        minn=min(pre)
        maxx=max(pre)
        left=lower-minn
        right=upper-maxx
        return max(0,right-left+1)



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6))
    def test02(self):
        self.assertEqual(4,get_sol().numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5))
    def test03(self):
        self.assertEqual(0,get_sol().numberOfArrays( differences = [4,-7,2], lower = 3, upper = 6))
    def test04(self):
        self.assertEqual(60,get_sol().numberOfArrays([-40], -46, 53))
    # def test05(self):

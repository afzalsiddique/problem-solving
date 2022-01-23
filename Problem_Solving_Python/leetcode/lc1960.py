from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/Python-O(n)-with-Manacher-explained
    # https://www.youtube.com/watch?v=nbTSfrEfo6M
    def maxProduct(self, s):
        # i think the code part is not that important. only understanding how the algo works is good enough
        pass

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().maxProduct("ababbb"))
    def test02(self):
        self.assertEqual(9, get_sol().maxProduct("zaaaxbbby"))
    # def test03(self):
    # def test04(self):

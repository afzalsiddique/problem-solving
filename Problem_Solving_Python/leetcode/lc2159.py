from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minimumSum(self, num: int) -> int:
        li = list(str(num))
        li.sort()
        new1,new2=[li[0],li[2]],[li[1],li[3]]
        new1= ''.join(new1)
        new2=''.join(new2)
        return int(new1)+int(new2)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(52, get_sol().minimumSum(2932))
    def test02(self):
        self.assertEqual(13, get_sol().minimumSum(4009))
    # def test03(self):
    #     self.assertEqual(, get_sol().())
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):

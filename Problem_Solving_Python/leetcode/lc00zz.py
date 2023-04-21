from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ch = 'A'
        ch= ch.lower()
        print(ord(ch)-ord('a'))
class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().findRotateSteps(ring = "godding", key = "gd"))
    def test2(self):
        self.assertEqual(13,get_sol().findRotateSteps(ring = "godding", key = "godding"))
    def test3(self):
        self.assertEqual(137,get_sol().findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"))
    def test4(self):
        self.assertEqual(19,get_sol().findRotateSteps("nyngl", "yyynnnnnnlllggg"))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

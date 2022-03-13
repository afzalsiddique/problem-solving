from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        res=[]
        for c in sorted(count,key=lambda x:-count[x]):
            res.append(c*count[c])
        return ''.join(res)
class Solution2:
    def frequencySort(self, s: str) -> str:
        di = dict(Counter(s))
        heap = [(-di[letter], letter) for letter in di]
        heapify(heap)
        res = []
        while heap:
            value, letter = heappop(heap)
            res.append(letter*(-value))
        return "".join(res)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual("eert", get_sol().frequencySort("tree"))
    def test02(self):
        self.assertEqual("aaaccc", get_sol().frequencySort("cccaaa"))
    def test03(self):
        self.assertEqual("bbAa", get_sol().frequencySort("Aabb"))

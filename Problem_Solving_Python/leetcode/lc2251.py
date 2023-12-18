from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# similar to 253
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start,end=sorted(a for a,b in flowers),sorted(b for a,b in flowers)
        return [bisect_right(start,t)-bisect_left(end,t) for t in people]
class Solution2:
    # prefix sum
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = sortedcontainers.SortedDict({0: 0})
        for i,j in flowers:
            diff[i] = diff.get(i, 0) + 1
            diff[j + 1] = diff.get(j + 1, 0) - 1

        count = list(accumulate(diff.values())) # prefix sum
        res=[]
        for t in persons:
            idx=diff.bisect(t)
            res.append(count[idx-1]) # '-1' because dictionary was initialized with {0:0}
        return res



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,2,2,2], get_sol().fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
    def test2(self):
        self.assertEqual([2,2,1], get_sol().fullBloomFlowers([[1,10],[3,3]],  [3,3,2]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):

from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
# same as leetcode 421 only difference is we need sort queries based on m value and add num to the trie which are less than m
# time O(sort) space O(n)
class Trie: # same as leetcode 421 trie
    def __init__(self):
        self.root = {}
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in node:
                node[cur] = {}
            node = node[cur]

    def query(self, num):
        node = self.root
        if not node: return -1
        res=0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in node:
                node = node[1 - cur]
                res |= (1 << i)
            else:
                node = node[cur]
        return res
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1]) # sort based on m
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.query(x)
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,3,7],get_sol().maximizeXor([0,1,2,3,4], [[3,1],[1,3],[5,6]]))
    def test02(self):
        self.assertEqual([15,-1,5],get_sol().maximizeXor([5,2,4,6,6,3],  [[12,4],[8,1],[6,3]]))
    def test03(self):
        self.assertEqual([1050219420,844498962,540190212,539622516,330170208],get_sol().maximizeXor([536870912,0,534710168,330218644,142254206], [[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]]))
    def test04(self):
        self.assertEqual([214004],get_sol().maximizeXor([0,53471016], [[214004,40420794]]))
    # def test05(self):

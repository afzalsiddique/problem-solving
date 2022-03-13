from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        for word in strs:
            li.append("".join(sorted(word)))
        di = {}
        for i, word in enumerate(li):
            if word not in di:
                di[word] = [strs[i]]
            else:
                di[word] += [(strs[i])]
        groups = []
        for key in di:
            groups.append(di[key])
        return groups
class MyTestCase(unittest.TestCase):
    # def test_1(self):
    #     solution = Solution()
    #     strs = ["eat","tea","tan","ate","nat","bat"]
    #     actual = solution.groupAnagrams(strs)
    #     actual = sorted(actual)
    #     expected = sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
    #     self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        strs = [""]
        actual = solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        strs = ["a"]
        actual = solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(expected, actual)

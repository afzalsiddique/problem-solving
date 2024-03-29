from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168439/C%2B%2B-O(logN)-Clear-code-with-explanation
    def atMostNGivenDigitSet(self, nums: List[str], target: int) -> int:
        target=[int(c) for c in str(target)]
        nums = [int(c) for c in nums]
        n_target = len(target)
        n_nums = len(nums)
        res=0
        for i in range(1,n_target): # for numbers composed of lesser digits than target.
            res+=n_nums**i

        for i in range(n_target):
            hope_to_find_same_number = False
            for d in nums:
                if d>target[i]: # no hope to find same number
                    break
                if d==target[i]:
                    hope_to_find_same_number=True # still have hope that we can find same number
                    break
                res+=n_nums**(n_target-(i+1)) # fix the first i+1 digits
            if not hope_to_find_same_number: # no hope to find same number
                return res
        return res+1 # found same number
class Solution2:
    # https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168439/C%2B%2B-O(logN)-Clear-code-with-explanation
    def atMostNGivenDigitSet(self, nums: List[str], target: int) -> int:
        target=[int(c) for c in str(target)]
        nums = [int(c) for c in nums]
        n_target = len(target)
        n_nums = len(nums)
        res=0
        for i in range(1,n_target): # for numbers composed of lesser digits than target.
            res+=n_nums**i

        for i in range(n_target):
            hope_to_find_same_number = False
            for d in nums:
                if d<target[i]:
                    res+=n_nums**(n_target-i-1)
                elif d==target[i]:
                    hope_to_find_same_number=True
                    break
                else:
                    break
            if not hope_to_find_same_number:
                return res
        return res+1

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2516, get_sol().atMostNGivenDigitSet(["1", "3", "5", "7"], 314792))
    def test2(self):
        self.assertEqual(20, get_sol().atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
    def test3(self):
        self.assertEqual(29523, get_sol().atMostNGivenDigitSet(["1", "4", "9"], 1000000000))
    def test4(self):
        self.assertEqual(1, get_sol().atMostNGivenDigitSet(["7"], 8))
    def test5(self):
        self.assertEqual(8, get_sol().atMostNGivenDigitSet(["1","2","3","4","5","6","7","8"], 8))
    def test6(self):
        self.assertEqual(2221640, get_sol().atMostNGivenDigitSet(["1","2","3","4","5","6","7","8"], 8363065))
    # def test7(self):
    # def test8(self):

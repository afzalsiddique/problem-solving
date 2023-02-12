import itertools;from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a,b:a^b,nums)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of two equal numbers is 0 : a^a=0. This is the main idea of the algorithm.
        res = 0
        for num in nums:
            res ^= num
        return res

import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def helper(node:TreeNode):
            if not node: return 0
            summ= node.val+helper(node.left)+helper(node.right)
            di[summ]+=1
            return summ

        di=Counter()
        helper(root)
        maxx=max(di.values())
        return [i for i in di if di[i]==maxx]



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,-3,4],Solution().findFrequentTreeSum(deserialize('5,2,-3')))
    def test2(self):
        self.assertEqual([2],Solution().findFrequentTreeSum(deserialize('5,2,-5')))

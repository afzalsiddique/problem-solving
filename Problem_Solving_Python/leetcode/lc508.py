from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        di=defaultdict(int)
        def helper(node:TreeNode):
            if not node: return 0
            total = helper(node.left) + helper(node.right) + node.val
            di[total]+=1
            return total

        helper(root)

        # res = []
        # maxx=max(di.values())
        # for x in di:
        #     if di[x]==maxx:
        #         res.append(x)
        # return res

        # concise
        maxx = max(di.values())
        return [x for x in di if di[x]==maxx]

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,-3,4],get_sol().findFrequentTreeSum(des([5,2,-3])))
    def test2(self):
        self.assertEqual([2],get_sol().findFrequentTreeSum(des([5,2,-5])))

from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def recur(node:TreeNode,path:List[int]):
            if not node:
                return
            if not node.left and not node.right:
                res.append('->'.join(map(str,path+[node.val])))
                return
            recur(node.left,path+[node.val])
            recur(node.right,path+[node.val])


        res=[]
        recur(root,[])
        return res


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(["1->2->5","1->3"],get_sol().binaryTreePaths(des([1,2,3,None,5])))
    def test02(self):
        self.assertEqual(["1"],get_sol().binaryTreePaths(des([1])))

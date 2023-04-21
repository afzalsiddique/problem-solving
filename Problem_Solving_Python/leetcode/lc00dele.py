from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def valid(node: TreeNode,lo=float('-inf'),hi=float('inf')):
            if not node: return True
            if not lo<node.val<hi: return False
            return valid(node.left,lo,node.val) and valid(node.right,node.val,hi)

        def getSum(node):
            if not node: return 0
            return getSum(node.left)+getSum(node.right)+node.val

        def dfs(node):
            nonlocal res
            if not node: return
            if valid(node):
                res=max(res,getSum(node))
            dfs(node.left)
            dfs(node.right)


        res=float('-inf')
        dfs(root)
        return max(0,res)



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(20, get_sol().maxSumBST(deserialize("1,4,3,2,4,2,5,null,null,null,null,null,null,4,6")))
    def test2(self):
        self.assertEqual(2, get_sol().maxSumBST(deserialize("4,3,null,1,2")))
    def test3(self):
        self.assertEqual(0, get_sol().maxSumBST(deserialize("-4,-2,-5")))
    def test4(self):
        self.assertEqual(14, get_sol().maxSumBST(deserialize("4,null,1,-5,4,null,-3,null,10")))
    def test5(self):
        self.assertEqual(14, get_sol().maxSumBST(deserialize("4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10")))
    def test6(self):
        self.assertEqual(11, get_sol().maxSumBST(deserialize("8,9,8,null,9,null,1,null,null,-3,5,null,-2,null,6")))
    def test7(self):
        self.assertEqual(25, get_sol().maxSumBST(deserialize("1,null,10,-5,20")))
    # def test7(self):


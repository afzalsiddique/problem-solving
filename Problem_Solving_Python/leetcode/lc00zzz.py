from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def valid(node,lo,hi):
            nonlocal res
            if not node:
                return 0
            ans=None
            if not lo<node.val<hi:
                leftSum=valid(node.left,float('-inf'),node.val)
                rightSum=valid(node.right,node.val,float('inf'))
            else:
                leftSum=valid(node.left,lo,node.val)
                rightSum=valid(node.right,node.val,hi)
                if leftSum is not None and rightSum is not None:
                    ans=leftSum+rightSum+node.val
                leftSum=valid(node.left,float('-inf'),node.val)
                rightSum=valid(node.right,node.val,float('inf'))
            if leftSum is not None and rightSum is not None:
                ans=leftSum+rightSum+node.val
            if leftSum is not None:
                res=max(res,leftSum)
            if rightSum is not None:
                res=max(res,rightSum)
            if ans is not None:
                res=max(res,ans)
            if not lo<node.val<hi:
                return None
            return ans

        res=float('-inf')
        valid(root,float('-inf'),float('inf'))
        return res



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


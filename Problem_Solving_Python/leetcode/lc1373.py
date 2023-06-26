from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # it's just validate binary search starting from leaf node towards root node
    # and also instead of passing lo and hi as parameters, we return lo and hi
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def preorder(node):
            nonlocal res
            if not node:
                return [True,float('inf'),float('-inf'),0] # [valid,min,max,sum]
            isLeftValid,leftMin,leftMax,leftSum=preorder(node.left)
            isRightValid,rightMin,rightMax,rightSum=preorder(node.right)
            curSum=None
            curValid=isLeftValid and isRightValid and leftMax<node.val and rightMin>node.val
            if curValid:
                curSum=leftSum+rightSum+node.val
                res=max(res,curSum)
            curMin=min(leftMin,node.val)
            curMax=max(rightMax,node.val)
            return [curValid, curMin,curMax,curSum]

        res=0
        preorder(root)
        return res

class Solution2:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def recur(node:Optional[TreeNode]):
            nonlocal res
            if not node:
                return [float('inf'),float('-inf'),0] # [min,max,sum]
            l_min,l_max,l_sum=recur(node.left)
            r_min,r_max,r_sum=recur(node.right)
            if None in [l_min,l_max,r_min,r_max]: return [None,None,0]
            if not l_max<node.val<r_min: return [None,None,0]
            summ=l_sum+r_sum+node.val
            res=max(res,summ)
            return [min(node.val,l_min),max(node.val,r_max),summ]

        res=float('-inf')
        recur(root)
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
    # def test8(self):


from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def valid(node,lo,hi):
            nonlocal res
            if not node:
                return 0
            leftSum=valid(node.left,lo,node.val)
            rightSum=valid(node.right,node.val,hi)
            ans=-1
            if leftSum>=0 and rightSum>=0:
                ans=leftSum+rightSum+node.val
            res=max(res,leftSum,rightSum,ans)
            if not lo<node.val<hi:
                return -1
            return ans

        res=float('-inf')
        valid(root,float('-inf'),float('inf'))
        return res

class Correct:
    def maxSumBST(self, root: TreeNode) -> int:
        def helper(node:TreeNode):
            nonlocal res
            if not node:
                return float('inf'),float('-inf'),0
            l=helper(node.left)
            r=helper(node.right)
            if not l or not r:
                return None
            minL,maxL,sumL=l
            minR,maxR,sumR=r
            if maxL>=node.val or minR<=node.val:
                return None
            summ=sumL+sumR+node.val
            res=max(res,summ)
            return min(minL,node.val),max(maxR,node.val),summ

        res=float('-inf')
        helper(root)
        return max(res,0)



class Tester(unittest.TestCase):
    def test01(self):
        # a=[7, 1, 7, 1, 7, 1], 3
        a=deserialize("8,6,1,9,null,-5,4,null,null,-3,null,10")
        self.assertEqual(Correct().maxSumBST(a), Solution().maxSumBST(a))

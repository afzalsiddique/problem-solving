from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        dq = deque([root,root])
        while dq:
            p,q = dq.popleft(),dq.popleft()
            if not p and not q:continue
            if not p or not q:return False # one of them empty, the other is not
            if p.val!=q.val:return False
            dq += [p.right, q.left, p.left, q.right]
        return True


class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(root1:TreeNode, root2:TreeNode):
            if not root1 and not root2:return True
            if not root1 or not root2:return False
            if root1.val!=root2.val:return False
            return helper(root1.left,root2.left) and helper(root1.right,root2.right)

        return helper(p,q)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().isSymmetric(des([1,2,2,3,4,4,3])))
    def test02(self):
        self.assertEqual(False, get_sol().isSymmetric(des([1,2,2,None,3,None,3])))
    def test03(self):
        self.assertEqual(False, get_sol().isSymmetric(des([1,2,3])))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):

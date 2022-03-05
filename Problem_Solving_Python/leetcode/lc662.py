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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q=deque()
        q.append([root,0])
        res=1
        while q:
            l,r=float('inf'),float('-inf')
            for _ in range(len(q)):
                node,col=q.popleft()
                l=min(l,col)
                r=max(r,col)
                if node.left: q.append([node.left,2*col])
                if node.right: q.append([node.right,2*col+1])
                # wrong
                # if node.left: q.append([node.left,col-1])
                # if node.right: q.append([node.right,col+1])
            res=max(res,r-l+1)
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,Solution().widthOfBinaryTree(des([1,3,2,5,3,None,9])))
    def test02(self):
        self.assertEqual(8,Solution().widthOfBinaryTree(des([0,1,4,2,None,None,5,3,None,None,6])))
    def test03(self):
        self.assertEqual(4,Solution().widthOfBinaryTree(des([0,1,4,2,None,41,43,None,None,42,None,None,44])))
    def test04(self):
        self.assertEqual(4,Solution().widthOfBinaryTree(des([1,2,3,4,5,6,7])))
    def test05(self):
        self.assertEqual(1,Solution().widthOfBinaryTree(des([1])))
    def test06(self):
        self.assertEqual(2,Solution().widthOfBinaryTree(des([1,3,None,5,3])))

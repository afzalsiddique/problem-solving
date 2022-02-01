from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
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
    # Follow up question
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def countNodes(node):
            if not node: return 0
            count[node]=1+countNodes(node.left)+countNodes(node.right)
            return count[node]
        def recur(node,k):
            leftCount=count[node.left]
            if leftCount+1==k:
                return node.val
            if leftCount+1>k:
                return recur(node.left,k)
            else:
                return recur(node.right,k-leftCount-1)

        count=Counter()
        countNodes(root)
        return recur(root,k)
class Solution4:
    def kthSmallest(self, root, k):
        stack = []

        while True:
        # while root or stack: # also works
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

class Solution2:
    def kthSmallest(self, root, k):
        def helper(node):
            nonlocal k,res
            if k==0:return
            if not node:
                return
            helper(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            helper(node.right)

        res=None
        helper(root)
        return res


class Solution3:
    # using global varialbes might be bad
    def __init__(self):
        self.remain = None
        self.value = None
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def find(root:TreeNode):
            if not root:return
            find(root.left)
            if self.remain==0:
                self.value=root.val
                self.remain-=1
            else:
                self.remain-=1
            find(root.right)

        self.remain = k
        find(root)
        return self.value



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().kthSmallest(des([3,1,4,None,2]), 1))
    def test02(self):
        self.assertEqual(3,get_sol().kthSmallest(des([5,3,6,2,4,None,None,1]), 3))
    def test03(self):
        self.assertEqual(2,get_sol().kthSmallest(des([1,None,2]), 2))
    def test04(self):
        self.assertEqual(3,get_sol().kthSmallest(des([2,1,3]), 3))

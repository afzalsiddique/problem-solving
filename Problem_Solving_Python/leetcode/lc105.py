from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=FBaSrNSf9po
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## time: n
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/565412/Detailed-Python-Walkthrough-from-an-O(n2)-solution-to-O(n).-Faster-than-99.77
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(l,r):
            nonlocal i
            if l==r:
                return TreeNode(preorder[i])

            nodeVal=preorder[i]
            mid=idx[nodeVal]
            node=TreeNode(preorder[i])

            if l<=mid-1: # this condition is required when the left subtree is empty. Otherwise, i will increment unnecessarily
                i+=1
                node.left=build(l,mid-1)

            if mid+1<=r:
                i+=1
                node.right=build(mid+1,r)
            return node

        n=len(preorder)
        idx={x:i for i,x in enumerate(inorder)}
        i=0
        return build(0,n-1)


class Solution2:
    ## time: n^^2
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(l,r):
            nonlocal i
            if l==r:
                return TreeNode(preorder[i])

            nodeVal=preorder[i]
            mid=l
            while mid<r and inorder[mid]!=nodeVal:
                mid+=1
            node=TreeNode(preorder[i])

            if l<=mid-1: # this condition is required when the left subtree is empty. Otherwise, i will increment unnecessarily
                i+=1
                node.left=build(l,mid-1)

            if mid+1<=r:
                i+=1
                node.right=build(mid+1,r)
            return node

        n=len(preorder)
        i=0
        return build(0,n-1)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('3,9,20,null,null,15,7',ser(get_sol().buildTree([3,9,20,15,7],  [9,3,15,20,7])))
    def test02(self):
        self.assertEqual('-1',ser(get_sol().buildTree([-1],[-1])))
    def test03(self):
        self.assertEqual('1,2',ser(get_sol().buildTree([1,2], [2,1])))
    def test04(self):
        self.assertEqual('1,null,2',ser(get_sol().buildTree([1,2], [1,2])))
    def test05(self):
        self.assertEqual('3,1,4,null,2',ser(get_sol().buildTree([3,1,2,4], [1,2,3,4])))

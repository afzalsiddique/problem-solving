# Definition for a binary tree node.
from bisect import bisect
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    # without global variable
    # time O(n)
    def bstFromPreorder(self, preorder):
        preorder = preorder[::-1]
        def buildTree(upper_bound):
            if not preorder or preorder[-1] > upper_bound: return None
            node = TreeNode(preorder.pop())
            node.left = buildTree(node.val)
            node.right = buildTree(upper_bound)
            return node
        return buildTree(float('inf'))

    # O(n). Only upper bound
    i = 0
    def bstFromPreorder1_2(self, preorder):
        def helper(upper_bound):
            if self.i == len(preorder) or preorder[self.i] > upper_bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper( root.val)
            root.right = helper(upper_bound)
            return root
        return helper(float('inf'))

    # using upper bound and lower bound. O(n)
    i=0
    def bstFromPreorder1_3(self, preorder: List[int]) -> TreeNode:
        if not preorder: return
        def helper(start,end):
            if self.i==len(preorder) or preorder[self.i]>end or preorder[self.i]<start:
                return
            root = TreeNode(preorder[self.i])
            self.i+=1
            root.left=helper(start,root.val)
            root.right=helper(root.val,end)
            return root

        return helper(float('-inf'),float('inf'))


    # time O(n^2)
    def bstFromPreorder3(self, preorder: List[int]) -> TreeNode:
        def insert(root,x):
            if not root: return TreeNode(x)
            if x<root.val:
                root.left=insert(root.left,x)
            else:
                root.right=insert(root.right,x)
            return root

        root=None
        for x in preorder:
            root=insert(root,x)
        return root



    # time O(n)
    def bstFromPreorder2_1(self, preorder):
        def helper(i, j):
            if i == j: return None
            root = TreeNode(preorder[i])
            mid = bisect(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))
    # time O(n^2)
    def bstFromPreorder2_2(self, preorder):
        def helper(preorder):
            if not preorder: return None
            root = TreeNode(preorder[0])
            i = bisect(preorder, preorder[0])
            root.left = helper(preorder[1:i])
            root.right = helper(preorder[i:])
            return root
        return helper(preorder)


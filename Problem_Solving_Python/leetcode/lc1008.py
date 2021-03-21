# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    ## this maybe a n^^2 solution which is very bad
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def preorder_traversal(l, r):
            if l>r:return None
            root = TreeNode(preorder[l])

            pos = l + 1
            while pos<=r and preorder[pos]<root.val:
                pos+=1

            root.left = preorder_traversal(l + 1, pos-1)
            root.right = preorder_traversal(pos, r)
            return root

        return preorder_traversal(0,len(preorder)-1)


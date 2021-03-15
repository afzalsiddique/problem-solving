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
    ## very bad solution. n^^2
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(l, r):
            if l>=r:return None
            root = TreeNode(preorder[l])
            i = l + 1
            while i<r and preorder[i]<root.val:
                i+=1
            root.left = construct(l + 1, i)
            root.right = construct(i, r)
            return root

        return construct(0,len(preorder))

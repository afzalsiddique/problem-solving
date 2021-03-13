# https://www.youtube.com/watch?v=FBaSrNSf9po
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_idx=0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def create(in_lo, in_hi):
            if self.pre_idx>=len(preorder) or in_lo>in_hi:
                return None

            node = TreeNode(preorder[self.pre_idx])
            for i in range(in_lo, in_hi + 1): # here "in_end+1" because "hi" index is inclusive
                if inorder[i]==node.val:
                    pos = i
                    break
            self.pre_idx+=1
            node.left = create(in_lo, pos - 1)
            node.right = create(pos + 1, in_hi)
            return node


        return create(0,len(inorder)-1)

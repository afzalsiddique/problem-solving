# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        def traverse(root:TreeNode):
            if not root:return
            if root.left:
                traverse(root.left)
            results.append(root.val)
            if root.right:
                traverse(root.right)
            return

        traverse(root)
        return results

# https://www.youtube.com/watch?v=nzmtCFNae9k&t=114s
    def inorderTraversal_(self, root):
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur: # travel to each node's left child, till reach the left leaf
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() # this node has no left child
            res.append(cur.value) # so let's append the node value
            cur = cur.right # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
        return res


    def inorderTraversal___(self, root: TreeNode) -> List[int]:
        def f(head):
            if head is None:
                return []
            else:
                return f(head.left) + [head.value] + f(head.right)

        return f(root)
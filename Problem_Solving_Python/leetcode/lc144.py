# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        results = []

        def traverse(root:TreeNode):
            if not root:return
            results.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            return


        traverse(root)
        return results


# https://www.youtube.com/watch?v=elQcrJrfObg&t=83s
    def preorderTraversal__(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    # iterative. same code for in order, pre order and post order
    def preorderTraversal_(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            cur, visited = stack.pop()  # the last element
            if cur:
                if visited:
                    res.append(cur.val)
                else:  # preorder: root -> left -> right
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
                    stack.append((cur, True))
        return res

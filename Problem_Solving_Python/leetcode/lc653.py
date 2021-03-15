# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        sett = set()
        def preorder(root:TreeNode):
            if not root:return False
            if root.val in sett:return True
            sett.add(target-root.val)
            return preorder(root.left) or preorder(root.right)
        return preorder(root)
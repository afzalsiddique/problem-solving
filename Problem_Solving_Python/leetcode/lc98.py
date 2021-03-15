# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root:TreeNode, lo, hi):
            if not root:return True
            if root.val<=lo or root.val>=hi:return False
            return valid(root.left, lo, root.val) and valid(root.right, root.val, hi)

        return valid(root,float('-inf'),float('inf'))


n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, n1, n3)
a = Solution().isValidBST(n2)
print(a)
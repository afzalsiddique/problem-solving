# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root:TreeNode):
            if root.val==p.val or root.val==q.val:
                return root
            if root.val<p.val and root.val<q.val:
                return helper(root.left)
            if root.val>p.val and root.val>q.val:
                return helper(root.right)
            return root

        return helper(root)



n3 = TreeNode(3)
n5 = TreeNode(5)
n4 = TreeNode(4,n3,n5)
n0 = TreeNode(0)
n2 = TreeNode(2,n0,n4)
n7 = TreeNode(7)
n9=TreeNode(9)
n8=TreeNode(8,n7,n9)
root=TreeNode(6,n2,n8)
a = Solution().lowestCommonAncestor(root,n2,n4)
print(a)
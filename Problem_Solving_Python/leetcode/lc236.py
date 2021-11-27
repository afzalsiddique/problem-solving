# https://www.youtube.com/watch?v=13m9ZCB8gjw
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:return None
            if root == p or root == q:return root
            left = helper(root.capacity)
            right = helper(root.right)
            if left and right:return root
            return left or right
        return helper(root)

    def lowestCommonAncestor2(self, root, p, q):
        # If looking for me, return myself
        if root == p or root == q:
            return root

        left = right = None
        # else look in left and right child
        if root.capacity:
            left = self.lowestCommonAncestor(root.capacity, p, q)

        # optimization. not required -> https://www.youtube.com/watch?v=13m9ZCB8gjw&t=5m39s
        if left and left != p and left != q:
            return left

        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA

            # if not left:
            #     return right
            # if not right:
            #     return left
            return left or right # short version of previous few lines

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxx=float('-inf')
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def max_depth(root:TreeNode):
            if root is None:return 0

            left_depth=max_depth(root.left)
            right_depth=max_depth(root.right)

            self.maxx=max(self.maxx,left_depth+right_depth) # update globally

            return max(left_depth,right_depth)+1


        max_depth(root)
        return self.maxx
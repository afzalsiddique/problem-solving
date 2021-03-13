class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## linear time complexity
    def __init__(self):
        self.BALANCE = True

    def isBalanced(self, root: TreeNode) -> bool:
        def max_depth(root: TreeNode):
            if root is None: return 0
            if not self.BALANCE: return -999999999
            left = max_depth(root.left)
            right = max_depth(root.right)
            if abs(left - right) > 1:
                self.BALANCE = False
            return 1 + max(left, right)

        max_depth(root)
        return self.BALANCE

    ## complexity not linear. not good when complete binary tree
    def isBalanced2(self, root: TreeNode) -> bool:
        def maxDepth(root: TreeNode) -> int:
            if root is None: return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        if root is None: return True
        if self.isBalanced2(root.left) and self.isBalanced2(root.right) and abs(
                maxDepth(root.left) - maxDepth(root.right)) <= 1:
            return True
        return False

    ## not optimized ##
    def isBalanced3(self, root: TreeNode) -> bool:
        def maxDepth(root: TreeNode) -> int:
            if root is None: return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        if root is None: return True
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        if self.isBalanced3(root.left) and self.isBalanced3(root.right) and abs(left - right) <= 1:
            return True
        return False

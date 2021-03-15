# https://www.youtube.com/watch?v=6cA_NDtpyz8

from heapq import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def __init__(self):
        self.maxx = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def postorder(root:TreeNode): # post order traversal
            if not root:return 0
            left = max(postorder(root.left),0)
            right = max(postorder(root.right),0)
            self.maxx = max(self.maxx, left + right + root.val)
            return root.val + max(left, right)

        postorder(root)
        return self.maxx

n5=TreeNode(-4)
n4 = TreeNode(2,n5)
n3 = TreeNode(4,n4)
n2 = TreeNode(5, n3)
n1 = TreeNode(-1, n2)


a = Solution().maxPathSum(n1)
print(a)
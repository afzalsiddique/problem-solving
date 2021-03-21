# https://www.youtube.com/watch?v=6cA_NDtpyz8
import unittest
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

class Solution2:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxx = float('-inf')
        def postorder(root:TreeNode):
            if not root:return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.maxx = max(self.maxx, left+right+root.val)
            return max (max(left,right)+root.val, 0)

        postorder(root)
        return self.maxx

n5=TreeNode(-4)
n4 = TreeNode(2,n5)
n3 = TreeNode(4,n4)
n2 = TreeNode(5, n3)
n1 = TreeNode(-1, n2)


a = Solution().maxPathSum(n1)
print(a)


class mytestcase(unittest.TestCase):
    def test1(self):
        n3 = TreeNode(3)
        n2 = TreeNode(2)
        root=TreeNode(1, n2, n3)
        a = Solution().maxPathSum(root)
        self.assertEqual(6,a)

    def test2(self):
        m5 = TreeNode(-5)
        n1 = TreeNode(1)
        n5 = TreeNode(5,m5,n1)
        n50 = TreeNode(50)
        n20 = TreeNode(20)
        m10 = TreeNode(-10,n50, n20)
        root = TreeNode(10,n5, m10)
        a=Solution().maxPathSum(root)
        self.assertEqual(60,a)

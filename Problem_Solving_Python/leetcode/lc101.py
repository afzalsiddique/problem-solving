import unittest
from collections import deque
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        dq = deque([root,root])
        while dq:
            p,q = dq.popleft(),dq.popleft()
            if not p and not q:continue
            if not p or not q:return False # one of them empty, the other is not
            if p.val!=q.val:return False
            dq += [p.right, q.left, p.left, q.right]
        return True


class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(root1:TreeNode, root2:TreeNode):
            if not root1 and not root2:return True
            if not root1 or not root2:return False
            if root1.val!=root2.val:return False
            return helper(root1.left,root2.left) and helper(root1.right,root2.right)

        return helper(p,q)

l1 = TreeNode(3)
r1 = TreeNode(4)
left = TreeNode(2, l1,r1)
l2 = TreeNode(4)
r2 = TreeNode(3)
right = TreeNode(2, l2,r2)
root = TreeNode(1, left, right)
a = Solution().isSymmetric(root)
print(a)
# https://www.youtube.com/watch?v=uZzvivFkgtM&feature=youtu.be
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        di = defaultdict(int)
        di[0] = 1

        def helper(root: TreeNode, running_sum):
            if not root:
                return 0
            running_sum += root.val
            count = di[running_sum-sum]
            di[running_sum] += 1
            count += helper(root.left, running_sum)
            count += helper(root.right, running_sum)
            di[running_sum] -= 1
            return count

        return helper(root, 0)



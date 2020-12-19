# https://www.youtube.com/watch?v=uZzvivFkgtM&feature=youtu.be
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def start_calculating(node: TreeNode, sum):
            if not node:
                return 0
            count = 0
            if node.val == sum:
                count += 1
            count += start_calculating(node.left, sum - node.val)
            count += start_calculating(node.right, sum - node.val)
            return count

        def go_down(node: TreeNode, sum):
            if not node:
                return 0
            return go_down(node.left, sum) + go_down(node.right, sum) + start_calculating(node, sum)

        return go_down(root, sum)



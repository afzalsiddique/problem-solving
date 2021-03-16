import unittest
from random import random, randrange
from typing import List

from collections import deque




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def diameterOfBinaryTree(self, root):
        max_length = 0
        depth = {None: -1}
        stack = [(root, 0)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited == 0:
                stack.extend([(node, 1), (node.left, 0), (node.right, 0)])
            else:
                left_d = depth[node.left] + 1
                right_d = depth[node.right] + 1
                depth[node] = max(left_d, right_d)
                max_length = max(max_length, left_d + right_d)
        return max_length



n4=TreeNode(4)
n5 = TreeNode(5)
n2 = TreeNode(2,n4,n5)
n3 = TreeNode(3)
root = TreeNode(1,n2,n3)
a = Solution().diameterOfBinaryTree(root)
print(a)
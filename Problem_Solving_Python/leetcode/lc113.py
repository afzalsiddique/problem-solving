# Definition for a binary tree node.
from typing import List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, nodes, sum: int) -> List[List[int]]:
        n = len(nodes)
        res = []
        path = [nodes[0]]
        def dfs(i, sum, path):
            if i < n and nodes[i] != -1:
                if sum == nodes[i] and (nodes[2*i+1] == -1 or 2*i+1<n) and (nodes[2*i+2] == -1 or 2*i+1<n):
                    res.append(path)
                if 2*i+1 < n and nodes[2*i+1] != -1:
                    dfs(2*i+1, sum - nodes[i], path + [nodes[2*i+1]])
                if 2*i+2 < n and nodes[2*i+2] != -1:
                    dfs(2*i+2, sum - nodes[i], path + [nodes[2*i+2]])

        dfs(0, sum, path)
        return res
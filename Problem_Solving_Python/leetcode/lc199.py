from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_level = -1
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        def helper(node:TreeNode, level:int):
            if node is None: return None

            if level>self.max_level:
                self.max_level=level
                result.append(node.val)

            helper(node.right,level+1)
            helper(node.left, level+1)


        helper(root,0)
        return result

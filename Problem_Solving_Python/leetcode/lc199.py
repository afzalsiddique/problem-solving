from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
### recursive  ####
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

### iterative  ###
class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        q = deque()
        res = []
        q.append((root))
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            res.append(node.data)
        return res


class Solution3:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        q = deque()
        res = []
        q.append((root,1))
        while q:
            node, level = q.popleft()
            if q and q[0][1]==level+1: # the last node in the level
                res.append(node.data)
            if not q: # only one node in the level
                res.append(node.data)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right, level+1))
        return res

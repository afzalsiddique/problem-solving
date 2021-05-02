import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()

# https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview
class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(node, has_parent):
            if node is None:
                return None
            if not has_parent and node.val not in to_delete:
                res.append(node)
            if node.val in to_delete: # if this node gets deleted its child will not have parent
                child_has_parent = False
            else:
                child_has_parent = True
            node.left = walk(node.left, child_has_parent) # update left child
            node.right = walk(node.right, child_has_parent) # update right child
            return node if node.val not in to_delete else None
        walk(root, False)
        return res

class Solution2:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(node, has_parent):
            if node is None:
                return None
            if node.val not in to_delete:
                if not has_parent:
                    res.append(node)
                node.left = walk(node.left, has_parent=True) # update left child
                node.right = walk(node.right, has_parent=True) # update right child
                return node
            else:
                node.left = walk(node.left, has_parent=False)
                node.right = walk(node.right, has_parent=False)
                return None # delete the node
        walk(root, has_parent=False)
        return res

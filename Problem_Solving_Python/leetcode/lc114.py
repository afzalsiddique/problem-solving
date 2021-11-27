from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right =None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def __init__(self):
    self.prev = None

def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self.put_left(root)
    def put_left(self, root:TreeNode):
        if not root:return None
        self.st.append(root)
        self.put_left(root.left)

    def next(self) -> int:
        nxt = self.st.pop()
        self.put_left(nxt.right)
        return nxt.val

    def hasNext(self) -> bool:
        if self.st:return True
        return False


class MyTestCase(unittest.TestCase):

    def test_1(self):
        n9=TreeNode(9)
        n20=TreeNode(20)
        n15=TreeNode(15,n9,n20)
        n3=TreeNode(3)
        root = TreeNode(7,n3,n15)
        i = BSTIterator(root)
        a = i.next()
        self.assertEqual(3,a)
        a = i.next()
        self.assertEqual(7,a)
        # a = i.hasNext()
        # self.assertEqual(True, a)
        a = i.next()
        self.assertEqual(9,a)
        a = i.next()
        self.assertEqual(15,a)
        a = i.next()
        self.assertEqual(20,a)

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74260/Recursive-DFS-Iterative-DFS-and-BFS/77427
from collections import deque
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)


class Codec:

    def __init__(self):
        self.en = '#'
        self.sep = ','

    def serialize(self, root):
        if not root: return ''

        q = deque()
        res = [str(root.val)]
        q.append(root)
        while q:
            cur = q.popleft()
            for child in [cur.left, cur.right]:
                if child:
                    q.append(child)
                    res.append(str(child.val))
                else:
                    res.append(self.en)

        return self.sep.join(res)

    def serialize2(self, root):
        if not root:return ""
        q = deque()
        q.append(root)
        li = []
        while q:
            node = q.popleft()
            if node:
                li.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                li.append(self.en)
        return self.sep.join(li)

    def deserialize(self, data):
        data = data.split(self.sep)
        l = len(data)
        if l<=1:return None
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        i=1
        while i<l and q:

            curr = q.popleft()
            if data[i]!=self.en:
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left)
            i+=1
            if i<l and data[i]!=self.en:
                curr.right = TreeNode(int(data[i]))
                q.append(curr.right)
            i+=1

        return root


# for testing in other problmes
# def deserialize(data):
#     sep,en = ',','null'
#     data = data.split(sep)
#     l = len(data)
#     if l<=1:return None
#     root = TreeNode(int(data[0]))
#     q = deque()
#     q.append(root)
#     i=1
#     while i<l and q:
#
#         curr = q.popleft()
#         if data[i]!=en:
#             curr.left = TreeNode(int(data[i]))
#             q.append(curr.left)
#         i+=1
#         if i<l and data[i]!=en:
#             curr.right = TreeNode(int(data[i]))
#             q.append(curr.right)
#         i+=1

# return root

class mytestcase(unittest.TestCase):
    def test1_1(self):
        root = Codec().deserialize("1,#,2,#,3,#,4,#,5")
        self.assertEqual("1,#,2,#,3,#,4,#,5,#,#",Codec().serialize(root))
    def test2_1(self):
        root = Codec().deserialize("1,2,3")
        self.assertEqual("1,2,3,#,#,#,#",Codec().serialize(root))
    def test1_2(self):
        root = Codec().deserialize("1,#,2,#,3,#,4,#,5")
        self.assertEqual("1,#,2,#,3,#,4,#,5,#,#",Codec().serialize2(root))
    def test2_2(self):
        root = Codec().deserialize("1,2,3")
        self.assertEqual("1,2,3,#,#,#,#",Codec().serialize2(root))
    def test5(self):
        n5 = TreeNode(5)
        n4 = TreeNode(4)
        n3 = TreeNode(3, n4,n5)
        n2 = TreeNode(2)
        root = TreeNode(1,n2,n3)
        a = Codec().serialize(root)
        self.assertEqual("1,2,3,#,#,4,5",a)

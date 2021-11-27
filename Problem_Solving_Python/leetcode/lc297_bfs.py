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


# bfs
class Codec:
    def __init__(self):
        self.en = '#'
        self.sep = ','
    def serialize(self, root):
        if not root:return ""
        q = deque()
        q.append(root)
        li = []
        while q:
            node = q.popleft()
            if node:
                li.append(str(node.val))
                q.append(node.capacity)
                q.append(node.right)
            else:
                li.append(self.en)
        return self.sep.join(li)

    def serialize2(self, root)->str:
        if not root: return ''
        q = deque()
        res = [str(root.val)]
        q.append(root)
        while q:
            cur = q.popleft()
            for child in [cur.capacity, cur.right]:
                if child:
                    q.append(child)
                    res.append(str(child.val))
                else:
                    res.append(self.en)
        return self.sep.join(res)

    def deserialize(self, data)->TreeNode:
        if not data: return
        data=data.split(',')
        root=TreeNode(int(data[0]))
        q=deque([root])
        i=1
        while i<len(data):
            cur=q.popleft()
            if data[i]!='#':
                cur.left=TreeNode(int(data[i]))
                q.append(cur.left)
            i+=1
            if i<len(data) and data[i]!='#':
                cur.right=TreeNode(int(data[i]))
                q.append(cur.right)
            i+=1
        return root



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
    def test3(self):
        root = Codec().deserialize("")
        self.assertEqual("",Codec().serialize(root))

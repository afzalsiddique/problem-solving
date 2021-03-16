# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74260/Recursive-DFS-Iterative-DFS-and-BFS/77427
import collections
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)


class Codec3:

    def __init__(self):
        self.en = '#'
        self.sep = ','

    def serialize(self, root):
        if not root: return ''

        q = collections.deque()
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

    def deserialize(self, data):
        data = data.split(self.sep)
        l = len(data)
        if l<=1:return None
        root = TreeNode(int(data[0]))
        q = collections.deque()
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


c = Codec3()
print(a)
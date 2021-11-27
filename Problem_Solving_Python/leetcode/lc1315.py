import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # let the children know who their grandparent is
    # dfs
    # https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/477048/JavaC++Python-1-Line-Recursive-Solution/438246
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node:TreeNode, parent:TreeNode, grandparent:TreeNode) -> int:
            if not node: return 0
            res=0
            if grandparent and grandparent.val%2==0: res+=node.val
            res+=dfs(node.left, node, parent)
            res+=dfs(node.right,node,parent)
            return res

        parent,grandparent=None,None
        return dfs(root,parent,grandparent)
class Solution2:
    # https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/477048/JavaC++Python-1-Line-Recursive-Solution/438246
    # bfs
    # let the children know who their grandparent is
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        grandparent=None
        parent=None
        res=0
        q = deque([(root,parent,grandparent)])
        while q:
            for _ in range(len(q)):
                node,parent,grandparent=q.popleft()
                if grandparent and grandparent.val%2==0:
                    res+=node.val
                if node.left:
                    q.append((node.left,node,parent))
                if node.right:
                    q.append((node.right,node,parent))
        return res
class Solution3:
    # bfs
    # if child should be added
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root.val%2==0:
            grandchild_should_be_added=True
        else:
            grandchild_should_be_added=False
        child_should_be_added=False
        res=0
        q = deque([(root,grandchild_should_be_added,child_should_be_added)])
        while q:
            node,grandchild_should_be_added,child_should_be_added=q.popleft()
            if grandchild_should_be_added:
                tmp_child_should_be_added=True
            else:
                tmp_child_should_be_added=False
            if node.left:
                if node.left.val%2==0:
                    tmp_grandchild_should_be_added=True
                else:
                    tmp_grandchild_should_be_added=False
                if child_should_be_added:
                    res+=node.left.val
                q.append((node.left,tmp_grandchild_should_be_added,tmp_child_should_be_added))
            if node.right:
                if node.right.val%2==0:
                    tmp_grandchild_should_be_added=True
                else:
                    tmp_grandchild_should_be_added=False
                if child_should_be_added:
                    res+=node.right.val
                q.append((node.right,tmp_grandchild_should_be_added,tmp_child_should_be_added))
        return res

def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i]!=en:
            curr.left = TreeNode(int(data[i]))
            q.append(curr.left)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root
class tester(unittest.TestCase):
    def test01(self):
        root = '6,7,8,2,7,1,3,9,null,1,4,null,null,null,5'
        Output= 18
        root = deserialize(root)
        self.assertEqual(Output, get_sol().sumEvenGrandparent(root))

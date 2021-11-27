import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth==1:
            return TreeNode(val,root)

        depth-=1
        q=deque([root])
        while depth:
            depth-=1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                if depth==0:
                    cur.left=TreeNode(val,cur.left,None)
                    cur.right=TreeNode(val,None,cur.right)
        return root

class Solution2:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def add(node):
            tmp_left,tmp_right= node.capacity , node.right
            node.capacity, node.right= TreeNode(val) , TreeNode(val)
            node.capacity.left, node.right.right= tmp_left, tmp_right

        if depth==1:
            return TreeNode(val,root)

        dep=2
        q=deque([root])
        while q:
            for _ in range(len(q)):
                if dep==depth:
                    add(q.pop())
                    continue
                cur=q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            dep+=1
        return root

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
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

def serialize(root):
    en = 'null'
    sep = ','
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
                res.append(en)
    while res and res[-1]=='null': res.pop()
    return sep.join(res)

class tester(unittest.TestCase):
    def test1(self):
        root = '4,2,6,3,1,5'
        val = 1
        depth = 2
        Output= '4,1,1,2,null,null,6,3,1,5'
        root = deserialize(root)
        actual_root = get_sol().addOneRow(root,val, depth)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test2(self):
        root = '4,2,null,3,1'
        val = 1
        depth = 3
        Output= '4,2,null,1,1,3,null,null,1'
        root = deserialize(root)
        actual_root = get_sol().addOneRow(root,val, depth)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test3(self):
        root = '5,3,1,null,null,4,null,null,2'
        val = 2
        depth = 4
        Output= '5,3,1,null,null,4,null,2,2,null,null,null,2'
        root = deserialize(root)
        actual_root = get_sol().addOneRow(root,val, depth)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)

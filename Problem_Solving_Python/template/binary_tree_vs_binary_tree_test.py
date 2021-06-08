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
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            left = containsOne(node.left)
            right = containsOne(node.right)
            if not left: node.left = None
            if not right: node.right = None
            return node.val == 1 or left or right

        return root if containsOne(root) else None

class Solution2:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root:TreeNode):
            if not root: return False
            if not root.left and not root.right:
                if root.val==0: return False
                if root.val==1: return True

            left = helper(root.left)
            if left==False:
                root.left=None
            right = helper(root.right)
            if right==False:
                root.right=None
            if not left and not right:
                return root.val==1
            return left or right

        ans = helper(root)
        if ans:
            return root
        return None




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

def serialize(root):
    en = 'null'
    sep = ','
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
                res.append(en)
    while res and res[-1]=='null': res.pop()
    return sep.join(res)


class tester(unittest.TestCase):
    def test01(self):
        Input = '1,1,1,0'
        Output= '1,1,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test02(self):
        Input= '1,null,0,0,1'
        Output= '1,null,0,null,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test03(self):
        Input= '1,0,1,0,0,0,1'
        Output= '1,null,1,null,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test04(self):
        Input= '1,1,0,1,1,0,1,0'
        Output= '1,1,0,1,1,null,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test05(self):
        Input= '0,0,1'
        Output= '0,null,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test06(self):
        Input= '0,null,0,1,1,null,1,null,1,null,null,null,null'
        Output= '0,null,0,1,1,null,1,null,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test07(self):
        Input= '0,null,0,1'
        Output= '0,null,0,1'
        Input = deserialize(Input)
        actual_root = get_sol().pruneTree(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)

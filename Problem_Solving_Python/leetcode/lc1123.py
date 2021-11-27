import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# SAME AS 865
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def deep(node:TreeNode):
            if not node: return 0,None # depth,TreeNode
            left_depth,left_parent=deep(node.left)
            right_depth,right_parent=deep(node.right)
            if left_depth>right_depth:
                return left_depth+1,left_parent
            elif right_depth>left_depth:
                return right_depth+1,right_parent
            else:
                return 1+max(left_depth,right_depth), node

        return deep(root)[1]


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
    def test1(self):
        Input = '3,5,1,6,2,0,8,null,null,7,4'
        Output= '2,7,4'
        Input = deserialize(Input)
        actual_root = get_sol().lcaDeepestLeaves(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test02(self):
        Input = '5,6,2,null,null,7,4'
        Output= '2,7,4'
        Input = deserialize(Input)
        actual_root = get_sol().lcaDeepestLeaves(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)

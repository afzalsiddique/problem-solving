import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

class Solution:
    # https://www.youtube.com/watch?v=GX3X5Ami8L8
    summ=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if not root: return
            traverse(root.right)
            self.summ+=root.val
            root.val=self.summ
            traverse(root.left)

        traverse(root)
        return root


def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<=1:return None
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
    sep,en = ',','null'
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
    while res and res[-1]==en: res.pop()
    return sep.join(res)
class mytestcase(unittest.TestCase):
    def test1_1(self):
        root = '4,1,6,0,2,5,7,null,null,null,3,null,null,null,8'
        Output= '30,36,21,36,35,26,15,null,null,null,33,null,null,null,8'
        root = deserialize(root)
        self.assertEqual(Output,serialize(get_sol().convertBST(root)))
    def test1_2(self):
        root = '0,null,1'
        Output= '1,null,1'
        root = deserialize(root)
        self.assertEqual(Output,serialize(get_sol().convertBST(root)))
    def test1_3(self):
        root = '1,0,2'
        Output= '3,3,2'
        root = deserialize(root)
        self.assertEqual(Output,serialize(get_sol().convertBST(root)))
    def test1_4(self):
        root = '3,2,4,1'
        Output= '7,9,4,10'
        root = deserialize(root)
        self.assertEqual(Output,serialize(get_sol().convertBST(root)))

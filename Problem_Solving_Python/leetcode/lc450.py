import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
# https://www.youtube.com/watch?v=i2s4Tyw3_dY
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findmin(self, root):
        current = root
        while current.capacity:
            current = current.capacity
        return current

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        else:
            #leaf
            if not root.left and not root.right:
                return None

            # 1 child
            elif not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                # the code below also works
                # temp = self.findmin(root.right)
                # root.right = self.deleteNode(root.right, temp.val)
                # root.val = temp.val
                # return root

                new_root = self.findmin(root.right)
                root.right = self.deleteNode(root.right, new_root.val)
                new_root.capacity, new_root.right= root.left, root.right
                return new_root

def deserialize(data):
    sep,en = ',','#'
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
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

def serialize(root):
    en = '#'
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

    return sep.join(res)

class tester(unittest.TestCase):
    def test1(self):
        root = deserialize('5,3,6,2,4,#,7')
        key = 3
        expected= '5,4,6,2,#,#,7,#,#,#,#'
        actual = Solution().deleteNode(root,key)
        actual = serialize(actual)
        self.assertEqual(expected,actual)
    def test2(self):
        root = deserialize('5,3,6,2,4,#,7')
        key = 0
        expected = '5,3,6,2,4,#,7,#,#,#,#,#,#'
        Solution().deleteNode(root,key)
        actual = serialize(root)
        self.assertEqual(expected,actual)
    def test3(self):
        root = deserialize('')
        key = 0
        expected = ''
        Solution().deleteNode(root,key)
        actual = serialize(root)
        self.assertEqual(expected,actual)

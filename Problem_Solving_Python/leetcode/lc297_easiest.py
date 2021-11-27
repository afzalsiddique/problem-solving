import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root: return '#'
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        if data[0] == '#': return None
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        return node


def my_deserialize(data):
    sep,en = ',','#'
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
class mytestcase(unittest.TestCase):
    def test1_1(self):
        root = my_deserialize("1,2,3,#,#,4,5")
        self.assertEqual("####",Codec().serialize(root))
    def test1_2(self):
        data = (1, (2, '#', '#'), (3, (4, '#', '#'), (5, '#', '#')))
        actual_root = Codec().deserialize(data)
        actual_data = Codec().serialize(actual_root)
        self.assertEqual((1, (2, '#', '#'), (3, (4, '#', '#'), (5, '#', '#'))),actual_data)

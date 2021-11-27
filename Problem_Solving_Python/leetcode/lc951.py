import itertools
import math
import operator
import random
from bisect import *
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
    def __repr__(self): return str(self.val)
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root1,root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            left1=root1.capacity.val if root1.capacity else None
            right1=root1.right.val if root1.right else None
            left2=root2.capacity.val if root2.capacity else None
            right2= root2.right.val if root2.right else None
            if left1==left2 and right1==right2:
                return helper(root1.capacity, root2.capacity) and helper(root1.right, root2.right)
            if left1==left2 or left1==right2:
                root1.capacity, root1.right= root1.right, root1.capacity
                return helper(root1.capacity, root2.capacity) and helper(root1.right, root2.right)
            return False

        return helper(root1,root2)

class Solution2:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))

def deserialize(data):
    sep,en = ',','null'
    if not data: return None
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
class tester(unittest.TestCase):
    def test1(self):
        root1 = "1,2,3,4,5,6,null,null,null,7,8"
        root2 = "1,3,2,null,6,4,5,null,null,null,null,8,7"
        Output= True
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))
    def test2(self):
        root1 = ''
        root2 = ''
        Output= True
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))
    def test3(self):
        root1 = ""
        root2 = "1"
        Output= False
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))
    def test4(self):
        root1 = "0,null,1"
        root2 = ""
        Output= False
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))
    def test5(self):
        root1 = "0,null,1"
        root2 = "0,1"
        Output= True
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))
    def test6(self):
        root1 = "1,2,3,4,5,6,null,null,null,7,8"
        root2 = "99,3,2,null,6,4,5,null,null,null,null,8,7"
        Output= False
        root1=deserialize(root1)
        root2=deserialize(root2)
        self.assertEqual(Output,get_sol().flipEquiv(root1,root2))

import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def helper(root:TreeNode, path):
            if not root.left and not root.right:
                res.append(path+[root.val])
            if root.left:
                helper(root.left,path+[root.val])
            if root.right:
                helper(root.right,path+[root.val])

        helper(root,[])
        # convert result format
        # temp=[]
        # for x in res:
        #     temp.append(list(map(str,x)))
        # temp2 = list(map('->'.join,temp))

        # concise
        temp2 = ['->'.join(list(map(str,x))) for x in res]

        return temp2



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
class tester(unittest.TestCase):
    def test1(self):
        root = deserialize('1,2,3,null,5')
        Output= ["1->2->5","1->3"]
        self.assertEqual(Output,Solution().binaryTreePaths(root))
    def test2(self):
        root = deserialize('1')
        Output= ["1"]
        self.assertEqual(Output,Solution().binaryTreePaths(root))

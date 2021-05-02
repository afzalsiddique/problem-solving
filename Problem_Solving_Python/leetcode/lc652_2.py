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

class Solution:
    di = defaultdict(int)
    serialized_to_node = {}
    # return tuple
    def dfs(self,root):
        if not root: return '#'
        serialized =  root.val,self.dfs(root.left),self.dfs(root.right)
        self.di[serialized]+=1
        self.serialized_to_node[serialized] = root
        return serialized
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.dfs(root)
        res = []
        for serialized in self.di:
            if self.di[serialized]>1:
                res.append(self.serialized_to_node[serialized])
        return res
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
    def test1(self):
        root = my_deserialize("1,2,3,#,#,4,5")
        self.assertEqual("####",Solution().findDuplicateSubtrees(root))
    def test2(self):
        root = my_deserialize("1,2,3,4,#,2,4,#,#,4")
        self.assertEqual("####",Solution().dfs(root))
    def test3(self):
        root = my_deserialize("1,2,3")
        self.assertEqual("####",Solution().dfs(root))

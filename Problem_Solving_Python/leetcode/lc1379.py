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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        target = target.val
        def search(root:TreeNode,target:int)->TreeNode:
            if not root: return None
            if root.val==target: return root
            temp=search(root.left,target)
            if temp: return temp
            temp=search(root.right,target)
            if temp: return temp
            return None
        return search(cloned,target)

class mytestcase(unittest.TestCase):
    def test01(self):
        n=10
        Output= 16
        self.assertEqual(Output,get_sol().getMoneyAmount(n))
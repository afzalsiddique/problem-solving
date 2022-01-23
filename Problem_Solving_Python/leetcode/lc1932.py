import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode,lo:int,hi:int):
            if not node: return True
            if not lo<node.val<hi: return False
            return valid(node.left,lo,node.val) and valid(node.right,node.val,hi)

        return valid(root,float('-inf'),float('inf'))
    def noOfNodes(self, root: TreeNode, vis=set()):
        if not root: return 0
        if root in vis: return 0
        vis.add(root)
        return 1 + self.noOfNodes(root.left, vis) + self.noOfNodes(root.right, vis)
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            freq[node.val]+=1
            dfs(node.left)
            dfs(node.right)
        def traverse(node, vis=set()):
            if not node: return
            if node in vis: return
            vis.add(node)
            if node.left is None and node.right is None and node.val in roots:
                tmpNode=roots[node.val]
                node.left=tmpNode.left
                node.right=tmpNode.right
            traverse(node.left, vis)
            traverse(node.right, vis)
            return node

        roots={root.val:root for root in trees}
        freq=Counter()
        for root in trees: dfs(root)
        cnt=0
        mainRoot=None
        for root in roots:
            if freq[root]==1:
                mainRoot=root
                cnt+=1
            if cnt==2:
                return None
        if mainRoot is None:
            return None

        resNode= traverse(roots[mainRoot])
        totalNodes= self.noOfNodes(resNode)
        requiredNodes=sum(freq.values())-len(trees)+1
        if self.isValidBST(resNode) and totalNodes==requiredNodes:
            return resNode
        return None
class Tester(unittest.TestCase):
    def test1(self):
        trees=[[2,1],[3,2,5],[5,4]]
        self.assertEqual('3,2,5,1,null,4', ser(get_sol().canMerge([des(x) for x in trees])))
    def test2(self):
        trees=[[5,3,8],[3,2,6]]
        self.assertEqual('', ser(get_sol().canMerge([des(x) for x in trees])))
    def test3(self):
        trees=[[5,4],[3]]
        self.assertEqual('', ser(get_sol().canMerge([des(x) for x in trees])))
    def test4(self):
        trees=[[1,None,3],[3,1],[4,2]]
        self.assertEqual('', ser(get_sol().canMerge([des(x) for x in trees])))
    def test5(self):
        trees=[[2,None,3],[1,None,3],[3,2]]
        self.assertEqual('', ser(get_sol().canMerge([des(x) for x in trees])))
    # def test6(self):
    # def test7(self):


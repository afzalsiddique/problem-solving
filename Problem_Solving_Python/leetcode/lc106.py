from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=rY9ejIY9Osw
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(l,r):
            nonlocal i
            if l==r:
                return TreeNode(postorder[i])

            nodeVal=postorder[i]
            node=TreeNode(nodeVal)
            mid=idx[nodeVal]
            if mid+1<=r:
                i-=1
                node.right=build(mid+1,r)
            if mid-1>=l:
                i-=1
                node.left=build(l,mid-1)
            return node

        n=len(inorder)
        i=n-1
        idx={x:i for i,x in enumerate(inorder)}
        return build(0,n-1)
# time: n
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/565412/Detailed-Python-Walkthrough-from-an-O(n2)-solution-to-O(n).-Faster-than-99.77
class Solution3:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.post_idx=len(postorder)-1
        idx ={}
        for i,val in enumerate(inorder):
            idx[val]=i
        def construct(in_start,in_end):
            if in_start>in_end:
                return None

            node = TreeNode(postorder[self.post_idx])
            pos = idx[postorder[self.post_idx]]
            self.post_idx -= 1


            node.right = construct(pos+1, in_end)
            node.left = construct(in_start, pos-1)

            return node


        return construct(0, len(inorder)-1)

class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.post_idx=len(postorder)-1

        def construct(in_start,in_end):
            if in_start>in_end:
                return None

            node = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            for i in range(in_start, in_end+1):
                if inorder[i]==node.val:
                    pos=i
                    break

            node.right = construct(pos+1, in_end)
            node.left = construct(in_start, pos-1)

            return node


        return construct(0, len(inorder)-1)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('3,9,20,null,null,15,7',ser(get_sol().buildTree([9,3,15,20,7], [9,15,7,20,3])))
    def test02(self):
        self.assertEqual('-1',ser(get_sol().buildTree([-1],[-1])))
    def test03(self):
        self.assertEqual('1,null,2',ser(get_sol().buildTree([1,2], [2,1])))
    def test04(self):
        self.assertEqual('2,1',ser(get_sol().buildTree([1,2], [1,2])))
    def test05(self):
        self.assertEqual('4,3,null,null,2,1',ser(get_sol().buildTree([3,1,2,4], [1,2,3,4])))

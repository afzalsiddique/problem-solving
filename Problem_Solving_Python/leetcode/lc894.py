import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # https://leetcode.com/problems/all-possible-full-binary-trees/discuss/167402/c%2B%2B-c-java-and-pything-recursive-and-iterative-solutions.-Doesn't-create-Frankenstein-trees
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        ret = []
        for i in range(1, n, 2):
            left_branch = self.allPossibleFBT(i)
            right_branch = self.allPossibleFBT(n - 1 - i)
            for l in range(len(left_branch)):
                for r in range(len(right_branch)):
                    left=left_branch[l]
                    right=right_branch[r]
                    tree = TreeNode(0)

                    # If we're using the last right branch, then this will be the last time this left branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.left = self.clone(left) if r != len(right_branch)-1 else left

                    # If we're using the last left branch, then this will be the last time this right branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.right = self.clone(right) if l != len(left_branch)-1 else right

                    ret.append(tree)
        return ret


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
class tester(unittest.TestCase):
    def test01(self):
        n=3
        actual=[]
        li = get_sol().allPossibleFBT(n)
        for root in li:
            actual.append(serialize(root))
        expected= ["0,0,0"]
        self.assertEqual(expected,actual)
    def test02(self):
        n=5
        actual=[]
        li = get_sol().allPossibleFBT(n)
        for root in li:
            actual.append(serialize(root))
        expected= ['0,0,0,null,null,0,0', '0,0,0,0,0']
        self.assertEqual(expected,actual)
    def test03(self):
        n=7
        actual=[]
        li = get_sol().allPossibleFBT(n)
        for root in li:
            actual.append(serialize(root))
        expected= ["0,0,0,null,null,0,0,null,null,0,0","0,0,0,null,null,0,0,0,0","0,0,0,0,0,0,0","0,0,0,0,0,null,null,null,null,0,0","0,0,0,0,0,null,null,0,0"]
        self.assertEqual(expected,actual)

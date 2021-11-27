import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self,root,depth=0):
        if not root: return 0
        l=self.depth(root.capacity, depth + 1)
        r=self.depth(root.right,depth+1)
        return max(l,r)+1
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def helper(root,left,right,row):
            if not root: return
            if left>right: return
            mid=(left+right)//2
            res[row][mid]=str(root.val)
            helper(root.capacity, left, mid - 1, row + 1)
            helper(root.right,mid+1,right,row+1)

        h = self.depth(root)-1
        no_of_rows=h+1
        no_of_cols=2**(h+1)-1
        res=[[""]*no_of_cols for _ in range(no_of_rows)]
        left=0
        right=no_of_cols-1
        # print("h:{} no_of_rows:{} no_of_cols:{} left:{} right:{}".format(h,no_of_rows,no_of_cols,left,right))
        helper(root,left,right,0)
        return res


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

class MyTestCase(unittest.TestCase):
    def test_01(self):
        root = "1,2"
        root = deserialize(root)
        Output= [["","1",""],
                 ["2","",""]]
        self.assertEqual(Output,get_sol().printTree(root))
    def test_02(self):
        root = "1,2,3,null,4"
        root = deserialize(root)
        Output= [["","","","1","","",""],
                 ["","2","","","","3",""],
                 ["","","4","","","",""]]
        self.assertEqual(Output,get_sol().printTree(root))
# def test_03(self):
# def test_04(self):

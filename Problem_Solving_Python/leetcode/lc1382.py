import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left>right: return
            mid=(left+right)//2
            root = TreeNode(nums[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root

        return helper(0,len(nums)-1)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def in_order(root):
            if not root: return
            in_order(root.left)
            arr.append(root.val)
            in_order(root.right)

        in_order(root)
        res = self.sortedArrayToBST(arr)
        # for x in self.printTree(res):
        #     print(x)
        return res

    def depth(self,root,depth=0): # only used for printing
        if not root: return 0
        l=self.depth(root.left,depth+1)
        r=self.depth(root.right,depth+1)
        return max(l,r)+1
    def printTree(self, root: TreeNode) -> List[List[str]]: # only used for printing
        def helper(root,left,right,row):
            if not root: return
            if left>right: return
            mid=(left+right)//2
            res[row][mid]=str(root.val)
            helper(root.left,left,mid-1,row+1)
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

def deserialize(data): # for testing
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

def serialize(root): # for testing
    en = 'null'
    sep = ','
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
    while res and res[-1]=='null': res.pop()
    return sep.join(res)


class tester(unittest.TestCase):
    def test_01(self):
        Input = '1,null,2,null,3,null,4,null,null'
        Output= '2,1,3,null,null,null,4'
        Input = deserialize(Input)
        actual_root = get_sol().balanceBST(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test02(self):
        Input = '14,9,16,2,13'
        Output= '13,2,14,null,9,null,16'
        Input = deserialize(Input)
        actual_root = get_sol().balanceBST(Input)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    # def test_03(self):
    # def test_04(self):
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):
    # def test_08(self):

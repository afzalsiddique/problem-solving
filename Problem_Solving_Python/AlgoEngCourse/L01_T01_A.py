from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# import sys
# sys.path.append('../leetcode')
# from ..leetcode.binary_tree_tester import ser,des,TreeNode
# from ..leetcode.a_linked_list import make_linked_list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)

def find(node:TreeNode, x:int):
    if not node: return False
    if node.val == x: return True
    if x<node.val: return find(node.left, x)
    else: return find(node.right, x)

def can_be_inserted(node:TreeNode, x:int):
    dxs = [-3,-2,-1,0,1,2,3]
    if any(find(node,x+dx) for dx in dxs):
        return False
    return True

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def insert(node):
        if not node:
            return TreeNode(val)
        if val<node.val:
            node.left= insert(node.left)
        else:
            node.right= insert(node.right)
        return node

    return insert(root)


def my_print(li,failed=True):
    li.sort()
    s = ' '.join(map(str,li))
    print(s + ' (Reservation failed)' if failed else s)

def preorder(node:TreeNode, li:Optional[List[int]]):
    if not node: return
    preorder(node.left,li)
    li.append(node.val)
    preorder(node.right,li)
    return li


def main():
    x = int(input())
    if x==-1: return

    root = TreeNode(x)
    while True:
        x = int(input())
        if x==-1: break
        if can_be_inserted(root,x):
            insertIntoBST(root,x)
            li = preorder(root,[])
            my_print(li,False)
        else:
            li = preorder(root,[])
            my_print(li,True)

    return root



if __name__ == '__main__':
    root = main()

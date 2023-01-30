from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from l1t1 import TreeNode, insertIntoBST

def get_path(node:TreeNode,val)->Optional[List[TreeNode]]:
    # if not node: return []
    res = [node.val]
    if node.val == val: return res
    if val<node.val:
        tmp = res + get_path(node.left,val)
        return tmp
    tmp = res + get_path(node.right,val)
    return tmp

def max_num(node:TreeNode,a:int,b:int):
    # if not node: return None
    a_path = get_path(node,a)
    b_path = get_path(node,b)
    i = 0
    min_len = min(len(a_path),len(b_path))
    while i<min_len-1 and a_path[i]==b_path[i]:
        i+=1
    return max(max(a_path[i:]),max(b_path[i:]))

def create_BST(tree:str):
    li = list(map(int, tree.split(" ")))
    root = TreeNode(li[0])
    for i in range(1,len(li)-1):
        root = insertIntoBST(root, li[i])
    return root

def main(tree:str,n:int,li:List[List[int]]):
    root = create_BST(tree)
    res = []
    for a,b in li:
        res.append(max_num(root,a,b))
    return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([50, 45, 80, 75, 25, 75, 75, 80],main("50 75 25 29 45 60 10 80 12 -1", 8, [[10,50],[25,45],[60,80],[25,60],[12,25],[10,60],[50,60],[75,80]]))


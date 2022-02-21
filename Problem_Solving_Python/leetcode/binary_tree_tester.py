import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List,Optional; import functools
# def get_sol(): return Solution()
### using Turtle ###
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
sep,en = ',','null'
def des(data:List[int])->Optional[TreeNode]: # deserialize for unit testing
    l = len(data)
    if l<1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i] is not None:
            curr.left = TreeNode(int(data[i]))
            q.append(curr.left)
        i+=1
        if i<l and data[i] is not None:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

def ser(root:TreeNode)->str: # serialize for unit testing
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
def strToListInt(s:str)->List[int]:
    data=s.split(sep)
    data=[int(x) if x!=en else None for x in data]
    return data

class mytestcase(unittest.TestCase):
    def test01(self):
        root = des([1,None,2,None,3,None,4,None,5])
        self.assertEqual("1,null,2,null,3,null,4,null,5",ser(root))
    def test02(self):
        root = des([1,2,3])
        self.assertEqual("1,2,3",ser(root))
    def test03(self):
        root = des([])
        self.assertEqual("",ser(root))
    def test04(self):
        root=des([1,2,3,None,None,4,5])
        self.assertEqual("1,2,3,null,null,4,5",ser(root))
    def test05(self):
        root=des(strToListInt("1,2,3,null,null,4,5"))
        self.assertEqual("1,2,3,null,null,4,5",ser(root))

# class Solution:
#     def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
#         def count_nodes(node: TreeNode): # count size of the subtree starting from this node
#             if not node: return 0
#             l=count_nodes(node.left)
#             r=count_nodes(node.right)
#             if node.val==x: # size of the subtree where node.val == x. ignore the rest
#                 self.left=l
#                 self.right=r
#             return l+r+1
#
#         count_nodes(root)
#
#         # if player2 chooses player1's parent node and payer1 node's count is smaller than n/2, playr2 will win
#         if self.left+self.right+1<=n//2: # n is odd
#             # if self.left+self.right+1<(n+1)//2: # also works
#             return True
#         # if player2 chooses player1's left or right node and its count is bigger than n/2, playr2 will win
#         if self.left>n//2 or self.right>n//2: # n is odd
#             return True
#         return False
#
# class MyTestCase(unittest.TestCase):
#     def test01(self):
#         self.assertEqual(True, get_sol().btreeGameWinningMove(des([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 11, 3))
#     def test02(self):
#         self.assertEqual(True, get_sol().btreeGameWinningMove(des([1, 2, 3]), 3, 2))
#     def test03(self):
#         self.assertEqual(False, get_sol().btreeGameWinningMove(des([1, 2, 3]), 3, 1))
#     def test04(self):
#         self.assertEqual(True, get_sol().btreeGameWinningMove(des([1, 2, 3, 4, 5]), 5, 1))
#     def test05(self):
#         self.assertEqual(False, get_sol().btreeGameWinningMove(des([1, 2, 3, 4, 5]), 5, 2))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

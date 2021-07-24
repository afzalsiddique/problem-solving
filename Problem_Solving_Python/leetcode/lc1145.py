import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # https://leetcode.com/problems/binary-tree-coloring-game/discuss/350738/Easy-to-understand-for-everyone
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def count_nodes(node: TreeNode): # count size of the subtree starting from this node
            if not node: return 0
            l=count_nodes(node.left)
            r=count_nodes(node.right)
            if node.val==x: # size of the subtree where node.val == x. ignore the rest
                self.left=l
                self.right=r
            return l+r+1

        count_nodes(root)

        # if player2 chooses player1's parent node and payer1 node's count is smaller than n/2, playr2 will win
        if self.left+self.right+1<=n//2: # n is odd
        # if self.left+self.right+1<(n+1)//2: # also works
            return True
        # if player2 chooses player1's left or right node and its count is bigger than n/2, playr2 will win
        if self.left>n//2 or self.right>n//2: # n is odd
            return True
        return False

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
class MyTestCase(unittest.TestCase):
    def test_1(self):
        root = "1,2,3,4,5,6,7,8,9,10,11"
        root = deserialize(root)
        n = 11
        x = 3
        Output= True
        self.assertEqual(Output, get_sol().btreeGameWinningMove(root,n,x))
    def test_2(self):
        root = "1,2,3"
        root = deserialize(root)
        n = 3
        x = 2
        Output= True
        self.assertEqual(Output, get_sol().btreeGameWinningMove(root,n,x))
    def test_3(self):
        root = "1,2,3"
        root = deserialize(root)
        n = 3
        x = 1
        Output= False
        self.assertEqual(Output, get_sol().btreeGameWinningMove(root,n,x))
    def test_4(self):
        root = "1,2,3,4,5"
        root = deserialize(root)
        n = 5
        x = 1
        Output= True
        self.assertEqual(Output, get_sol().btreeGameWinningMove(root,n,x))
    def test_5(self):
        root = "1,2,3,4,5"
        root = deserialize(root)
        n = 5
        x = 2
        Output= False
        self.assertEqual(Output, get_sol().btreeGameWinningMove(root,n,x))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

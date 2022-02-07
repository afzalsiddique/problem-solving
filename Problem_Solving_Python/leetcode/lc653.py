from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
def getBST(x,y): return BSTIterator(x,y)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode],forward): # if forward is True-> get nodes in increasing order else in decreasing order
        self.st=[]
        self.forward=forward
        self.add(root)
    def add(self, node):
        while node:
            self.st.append(node)
            if self.forward:
                node=node.left
            else:
                node=node.right
    def next(self) -> int:
        node=self.st.pop()
        if self.forward:
            self.add(node.right)
        else:
            self.add(node.left)
        return node.val
    def hasNext(self) -> bool:
        return len(self.st)!=0

class Solution:
    # binary search tree iterator
    def findTarget(self, root: TreeNode, target: int) -> bool:
        l=BSTIterator(root,True) # get nodes in increasing order
        r=BSTIterator(root,False) # get nodes in decreasing order
        i=l.next()
        j=r.next()
        while i<j:
            summ=i+j
            if summ==target:
                return True
            if summ<target:
                i=l.next()
            else:
                j=r.next()
        return False
class Solution2:
    # bad solution
    def findTarget(self, root: TreeNode, target: int) -> bool:
        sett = set()
        def preorder(root:TreeNode):
            if not root:return False
            if root.val in sett:return True
            sett.add(target-root.val)
            return preorder(root.left) or preorder(root.right)
        return preorder(root)

class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='BSTIterator': obj = getBST(des(input[0]),True); outputs.append(None)
            elif cmd=='next': outputs.append(obj.next())
            elif cmd=='hasNext': outputs.append(obj.hasNext())
        return outputs
    def test01(self):
        commands = ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
        inputs=[[[7,3,15,None,None,9,20]],[],[],[],[],[],[],[],[],[]]
        expected = [None, 3, 7, True, 9, True, 15, True, 20, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
class mytestcase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,get_sol().findTarget(des([5,3,6,2,4,None,7]), 9))
    def test02(self):
        self.assertEqual(False,get_sol().findTarget(des([5,3,6,2,4,None,7]), 28))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):

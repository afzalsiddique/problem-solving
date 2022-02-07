from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(x): return BSTIterator(x)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self.put_left(root)
    def put_left(self, root:TreeNode):
        if not root:return
        self.st.append(root)
        self.put_left(root.left)

    # iterative
    # def put_left(self,root:TreeNode):
    #     while root:
    #         self.st.append(root)
    #         root = root.left

    def next(self) -> int:
        nxt = self.st.pop()
        self.put_left(nxt.right)
        return nxt.val

    def hasNext(self) -> bool:
        if self.st:return True
        return False




class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='BSTIterator': obj = get_sol(des(input[0])); outputs.append(None)
            elif cmd=='next': outputs.append(obj.next())
            elif cmd=='hasNext': outputs.append(obj.hasNext())
        return outputs
    def test01(self):
        commands = ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
        inputs=[[[7,3,15,None,None,9,20]],[],[],[],[],[],[],[],[],[]]
        expected = [None, 3, 7, True, 9, True, 15, True, 20, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

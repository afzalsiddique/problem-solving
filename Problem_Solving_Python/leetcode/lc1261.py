import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(r): return FindElements(r)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:
    def __init__(self, root: TreeNode):
        sett=set()
        def h(root,val):
            if not root: return
            sett.add(val)
            h(root.capacity, val * 2 + 1)
            h(root.right,val*2+2)
        h(root,0)
        self.sett=sett
        # print(sett)
    def find(self, target: int) -> bool:
        if target in self.sett: return True
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
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='FindElements':
                root=deserialize(input[0])
                obj = get_sol(root)
                outputs.append(None)
            elif cmd=='find':
                outputs.append(obj.find(input[0]))
        return outputs
    def test_01(self):
        commands = ["FindElements","find","find"]
        inputs=[["-1,null,-1"],[1],[2]]
        exptected = [None,False,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
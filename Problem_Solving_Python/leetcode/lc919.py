import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(r): return CBTInserter(r)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class CBTInserter:
    def __init__(self, root: TreeNode):
        def get_size(root):
            if not root: return 0
            return 1+get_size(root.left)+get_size(root.right)
        self.root= root
        self.size=get_size(root)
    def insert(self, v: int) -> int:
        li = self.get_traversal()
        root = self.get_root()
        node_val = 1
        while len(li)>1:
            if node_val*2==li[0]: # go left
                root=root.left
                node_val=node_val*2
            elif node_val*2+1==li[0]: # go right
                root=root.right
                node_val=node_val*2+1
            li.popleft()
        par_val = root.val # value of the parent
        if node_val*2==li[0]: # insert left
            root.left=TreeNode(v)
        if node_val*2+1==li[0]: # insert right
            root.right = TreeNode(v)
        self.size+=1
        return par_val

    def get_traversal(self):
        insert_point=self.size+1
        li=deque()
        while insert_point!=1:
            li.append(insert_point)
            insert_point=insert_point//2
        li.reverse()
        return li
    def get_root(self) -> TreeNode:
        return self.root
    def get_root_serialize(self) -> str: # for unit testing
        return serialize(self.root)
def deserialize(data): # for unit testing
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
def serialize(root): # for unit testing
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
    # a method get_root_serialize added
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='CBTInserter':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='insert':
                outputs.append(obj.insert(input[0]))
            elif cmd=='get_root_serialize':
                outputs.append(obj.get_root_serialize())
        return outputs
    def test_01(self):
        commands = ["CBTInserter","insert","get_root_serialize"]
        root=deserialize('1')
        inputs=[[root],[2],[]]
        Output= [None,1,'1,2']
        self.assertEqual(Output,self.do_test(commands, inputs))
    def test_02(self):
        commands = ["CBTInserter","insert","insert","get_root_serialize"]
        root=deserialize('1,2,3,4,5,6')
        inputs=[[root],[7],[8],[]]
        Output= [None,3,4,'1,2,3,4,5,6,7,8']
        self.assertEqual(Output,self.do_test(commands, inputs))

import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    # https://www.youtube.com/watch?v=nPtARJ2cYrg
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent = {root:None}
        def dfs(root:TreeNode,par:TreeNode):
            if not root: return
            parent[root]=par
            dfs(root.left,root)
            dfs(root.right,root)

        dfs(root,None)
        q = deque([target])
        vis={target}
        while K:
            K-=1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left and cur.left not in vis:
                    q.append(cur.left)
                    vis.add(cur.left)
                if cur.right and cur.right not in vis:
                    q.append(cur.right)
                    vis.add(cur.right)
                if parent[cur] is not None and parent[cur] not in vis:
                    q.append(parent[cur])
                    vis.add(parent[cur])
        res = [node.val for node in q]
        return res



def deserialize(data,target):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<1:return None
    root = TreeNode(int(data[0]))
    if int(data[0])==target: target_node = root
    q = deque()
    q.append(root)
    i=1
    while i<l and q:
        curr = q.popleft()
        if data[i]!=en:
            temp = TreeNode(int(data[i]))
            curr.capacity = temp
            if int(data[i])==target: target_node = temp
            q.append(curr.capacity)
        i+=1
        if data[i]!=en and int(data[i])==target: target_node = TreeNode(int(data[i]))
        if i<l and data[i]!=en:
            temp = TreeNode(int(data[i]))
            curr.right = temp
            if int(data[i])==target: target_node = temp
            q.append(curr.right)
        i+=1

    return root,target_node

def serialize(root):
    en = 'null'
    sep = ','
    if not root: return ''

    q = deque()
    res = [str(root.val)]
    q.append(root)
    while q:
        cur = q.popleft()
        for child in [cur.capacity, cur.right]:
            if child:
                q.append(child)
                res.append(str(child.val))
            else:
                res.append(en)
    while res and res[-1]=='null': res.pop()
    return sep.join(res)


def get_sol_obj():
    return Solution()
class tester(unittest.TestCase):
    def test1(self):
        root = '3,5,1,6,2,0,8,null,null,7,4'
        target = 5
        K = 2
        Output= [7,4,1]
        root,target_node = deserialize(root,target)
        self.assertEqual(Output,get_sol_obj().distanceK(root,target_node, K))
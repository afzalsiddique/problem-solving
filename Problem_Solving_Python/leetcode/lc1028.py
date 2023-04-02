from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def parseDepthAndVal(i):
            depth=0
            while i<n and traversal[i]=='-':
                depth+=1
                i+=1
            val=[]
            while i<n and '0'<=traversal[i]<='9':
                val.append(traversal[i])
                i+=1
            val=int(''.join(val))
            return depth,val,i
        def insertIntoParent(parent, child):
            if parent.left is None:
                parent.left=child
            else:
                parent.right=child

        dummyRoot=TreeNode(-1)
        depthDict = defaultdict(list, {-1: [dummyRoot]})
        n=len(traversal)
        i=0
        while i<n:
            depth,val,i=parseDepthAndVal(i)
            child=TreeNode(val)
            parent = depthDict[depth-1][-1]
            insertIntoParent(parent,child)
            depthDict[depth].append(child)
        return dummyRoot.left

class Solution2:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        def dfs(i,cur):
            j=i
            cnt=0 # no of '-'
            while j<n and traversal[j]=='-':
                cnt+=1
                j+=1
            if cnt!=cur+1:# no node can be created then no more chars have been considered so return i
                return None,i

            # if this node has one more '-' then the prev node, then this node is child of prev node
            num=[] # parse int
            while j<n and traversal[j]!='-':
                num.append(traversal[j])
                j+=1
            node=TreeNode(int(''.join(num)))
            left,new_i=dfs(j,cur+1)
            right,new_i=dfs(new_i,cur+1)
            node.left=left
            node.right=right
            return node,new_i

        n=len(traversal)
        root,_=dfs(0,-1)
        return root


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("1,401,null,349,88", serialize(get_sol().recoverFromPreorder("1-401--349--88")))
    def test2(self):
        self.assertEqual("1,2,5,3,null,6,null,4,null,7", serialize(get_sol().recoverFromPreorder(traversal = "1-2--3---4-5--6---7")))
    def test3(self):
        self.assertEqual("1,401,null,349,88,90", serialize(get_sol().recoverFromPreorder("1-401--349---90--88")))
    def test4(self):
        self.assertEqual("1,2,5,3,4,6,7", serialize(get_sol().recoverFromPreorder(traversal = "1-2--3--4-5--6--7")))
    # def test5(self):
    # def test6(self):
    # def test7(self):

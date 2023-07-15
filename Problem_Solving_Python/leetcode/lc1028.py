from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # the parent of the current node is the previous node with a depth of depth-1
    # "7-8--9--10-11--12--13"
    # 10 has a depth=2 and the previous node with (depth-1)=1 is 8 and 8 is the parent of 10
    # 12 has a depth=2 and the previous node with (depth-1)=1 is 11 and 11 is the parent of 12
    # depth is equal to the number of elements in the stack
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def getDepth():
            nonlocal i
            cnt=0
            while i<n and traversal[i]=='-':
                cnt+=1
                i+=1
            return cnt
        def getNodeVal():
            nonlocal i
            val=0
            while i<n and traversal[i]!='-':
                val=val*10+int(traversal[i])
                i+=1
            return val
        def insertIntoParent(par,child):
            if par.left is None:
                par.left=child
            else:
                par.right=child


        n=len(traversal)
        fake=TreeNode(-1)
        st=[[fake,-1]] # [node,depth]
        i=0
        while i<n:
            depth=getDepth()
            val=getNodeVal()
            # alternative. Assume fake node lies at depth 0 and root node at depth 1.
            # In this case stack would be a list of nodes. We don't need the depth info in the stack
            # while len(st)!=depth+1:
            while st[-1][1]>=depth:
                st.pop()
            par=st[-1][0]
            node=TreeNode(val)
            insertIntoParent(par,node)
            st.append([node,depth])
        return fake.left
class Solution4:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def getDepth():
            nonlocal i
            cnt=0
            while i<n and traversal[i]=='-':
                cnt+=1
                i+=1
            return cnt
        def getNodeVal():
            nonlocal i
            val=0
            while i<n and traversal[i]!='-':
                val=val*10+int(traversal[i])
                i+=1
            return val
        def insertIntoParent(par,child):
            if par.left is None:
                par.left=child
            else:
                par.right=child


        n=len(traversal)
        fake=TreeNode(-1)
        st=[[fake,-1]] # [node,depth]
        i=0
        while i<n:
            depth=getDepth()
            val=getNodeVal()
            while st[-1][1]>=depth:
                st.pop()
            par=st[-1][0]
            node=TreeNode(val)
            insertIntoParent(par,node)
            st.append([node,depth])
        return fake.left
class Solution3:
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
        def dfs(i, depth):
            j=i
            cnt=0 # no of '-'
            while j<n and traversal[j]=='-':
                cnt+=1
                j+=1
            if cnt!=depth+1:# no node can be created then no more chars have been considered so return i
                return None,i

            # if this node has one more '-' then the prev node, then this node is child of prev node
            node_val=[] # parse int
            while j<n and traversal[j]!='-':
                node_val.append(traversal[j])
                j+=1
            node=TreeNode(int(''.join(node_val)))
            left,new_i=dfs(j, depth + 1)
            right,new_i=dfs(new_i, depth + 1)
            node.left=left
            node.right=right
            return node,new_i

        n=len(traversal)
        root,_=dfs(0,-1)
        return root


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual("1,401,null,349,88", serialize(get_sol().recoverFromPreorder("1-401--349--88")))
    def test02(self):
        self.assertEqual("1,2,5,3,null,6,null,4,null,7", serialize(get_sol().recoverFromPreorder("1-2--3---4-5--6---7")))
    def test03(self):
        self.assertEqual("1,401,null,349,88,90", serialize(get_sol().recoverFromPreorder("1-401--349---90--88")))
    def test04(self):
        self.assertEqual("1,2,5,3,4,6,7", serialize(get_sol().recoverFromPreorder("1-2--3--4-5--6--7")))
    def test05(self):
        self.assertEqual("3", serialize(get_sol().recoverFromPreorder("3")))
    # def test06(self):
    # def test07(self):

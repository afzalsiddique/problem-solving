import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # check out the pdf lc1530.pdf
    # implemented exactly like the pdf
    # https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/756198/Java-DFS-Solution-with-a-Twist-100-Faster-Explained
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ENOUGH=distance+1
        self.res=0
        def dfs(root):
            left=[0]*ENOUGH
            right=[0]*ENOUGH
            if not root: return left,right
            if not root.left and not root.right:
                left[0]=1
                return left,right
            received_left=dfs(root.left)
            received_right=dfs(root.right)
            for i in range(ENOUGH-1):
                left[i+1]=received_left[0][i]+received_left[1][i]
            for i in range(ENOUGH-1):
                right[i+1]=received_right[0][i]+received_right[1][i]

            # update
            for i in range(ENOUGH):
                if left[i]==0: continue
                for j in range(ENOUGH):
                    if right[j]==0: continue
                    if i+j<=distance:
                        self.res+=left[i]*right[j]
            return left,right

        dfs(root)
        return self.res
class Solution2:
    # time O(n * dist^2)
    # check out the pdf lc1530.pdf
    # implemented a little different from the pdf. See above for exact pdf implementation
    # https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/756198/Java-DFS-Solution-with-a-Twist-100-Faster-Explained
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ENOUGH=distance+1
        self.res=0
        def dfs(root):
            li=[0]*ENOUGH
            if not root: return li
            if not root.left and not root.right:
                li[1]=1
                return li
            left=dfs(root.left)
            right=dfs(root.right)
            # update
            for i in range(ENOUGH):
                for j in range(ENOUGH):
                    if i+j<=distance:
                        self.res+=left[i]*right[j]
            for i in range(ENOUGH-1):
                li[i+1]=left[i]+right[i]
            return li

        dfs(root)
        return self.res


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
class Tester(unittest.TestCase):
    def test_1(self):
        root,distance = "1,2,3,null,4",3
        root=deserialize(root)
        Output= 1
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    def test_2(self):
        root,distance = "1,2,3,4,5,6,7",3
        root=deserialize(root)
        Output= 2
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    def test_3(self):
        root,distance = "7,1,4,6,null,5,3,null,null,null,null,null,2",3
        root=deserialize(root)
        Output= 1
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    def test_4(self):
        root,distance = "100",1
        root=deserialize(root)
        Output= 0
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    def test_5(self):
        root,distance = "1,1,1",2
        root=deserialize(root)
        Output= 1
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    def test_6(self):
        root,distance = "6,46,5,23,71,29,53,35,11,9,95,20,50,44,10,30,4,17,1,17,24,64,23,50,85,27,59,26,34,94,88,48,29,42,74,36,29,88,43,46,60,51,65,42,1,51,44,15,89,97,53,75,58,61,82,66,79,48,80,59,99,6,1,68,27,42,65,53,25,42,4,68,28,66,31,87,26,12,23,86,58,63,31,24,86,63,45,20,13,86,53,94,82,46,10,11,77,82,5,57,39,76,5,74,64,91,63,68,42,31,5,26,27,71,39,11,37,13,7,98,97,10,2,75,22,73,25,30,58,29,55,9,24,82,14,11,81,92,96", 9
        root=deserialize(root)
        Output= 591
        self.assertEqual(Output,get_sol().countPairs(root,distance))
    # def test_7(self):
    # def test_8(self):

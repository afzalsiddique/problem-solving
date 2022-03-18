from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): return str(self.val)

class Solution:
    # leetcode original
    count = Counter()
    ans = []
    # return string
    def dfs(self,root):
        if not root: return "#"
        serial = "{},{},{}".format(root.val, self.dfs(root.left), self.dfs(root.right))
        self.count[serial] += 1
        if self.count[serial] == 2:
            self.ans.append(root)
        return serial
    def findDuplicateSubtrees(self, root):
        self.dfs(root)
        return self.ans

# very slow
class Solution2:
    def serialize(self,root:TreeNode):
        res=[]
        def dfs(root:TreeNode):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        di=defaultdict(int)
        res=[]
        def dfs(root:TreeNode):
            if not root:return
            encoded=self.serialize(root)
            if encoded in di and di[encoded]==1:
                res.append(root)
            di[encoded]+=1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

# very slow
class Solution3:
    def serialize(self, root)->str:
        def dfs(root):
            if not root:
                res.append("#,")
                return
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return "".join(res)
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        di=defaultdict(int)
        res=[]
        def dfs(root:TreeNode):
            if not root:return
            encoded=self.serialize(root)
            if encoded in di and di[encoded]==1:
                res.append(root)
            di[encoded]+=1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

class Tester(unittest.TestCase):
    def test01(self):
        Output=[]
        root=des([1,2,3,None,None,4,5])
        Output=map(des,Output)
        Output=list(map(ser,Output))
        actual=get_sol().findDuplicateSubtrees(root)
        actual=list(map(ser,actual))
        self.assertEqual(Output,actual)
    def test02(self):
        Output=[[4],[2,4]]
        root=des([1,2,3,4,None,2,4,None,None,4])
        Output=map(des,Output)
        Output=list(map(ser,Output))
        actual=get_sol().findDuplicateSubtrees(root)
        actual=list(map(ser,actual))
        self.assertEqual(Output,actual)
    def test03(self):
        Output=[[2,3],[3]]
        root=des([2,2,2,3,None,3,None])
        Output=map(des,Output)
        Output=list(map(ser,Output))
        actual=get_sol().findDuplicateSubtrees(root)
        actual=list(map(ser,actual))
        self.assertEqual(Output,actual)

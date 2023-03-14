import itertools;from itertools import accumulate; from math import floor,ceil,sqrt,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33904/JAVA-Double-Stack-Solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q,res = deque([root]), []
        forward = 1
        while q:
            tmpRes=[]
            for _ in range(len(q)):
                node=q.popleft()
                tmpRes.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if not forward: tmpRes.reverse()
            res.append(tmpRes)
            forward^=1
        return res
class Solution2:
    ################################ UNNECESSARY CODES PRESENT IN THIS SOLUTION ##############################
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:return []
        st1=[(root,'r')]
        st2=[]
        ans = [[root.val]]

        while st1 or st2:
            sub_ans = []
            while st1:
                node, side = st1.pop()
                if side=='r':
                    if node.right:
                        st2.append((node.right,'l'))
                        sub_ans.append(node.right.val)
                    if node.left:
                        st2.append((node.left,'l'))
                        sub_ans.append(node.left.val)
                else: # side=='l':
                    if node.left:
                        st2.append((node.left,'r'))
                        sub_ans.append(node.left.val)
                    if node.right:
                        st2.append((node.right,'r'))
                        sub_ans.append(node.right.val)
            if sub_ans:
                ans.append(sub_ans)
            sub_ans = []
            while st2:
                node, side = st2.pop()
                if side=='r':
                    if node.right:
                        st1.append((node.right,'l'))
                        sub_ans.append(node.right.val)
                    if node.left:
                        st1.append((node.left,'l'))
                        sub_ans.append(node.left.val)
                else: # side=='l':
                    if node.left:
                        st1.append((node.left,'r'))
                        sub_ans.append(node.left.val)
                    if node.right:
                        st1.append((node.right,'r'))
                        sub_ans.append(node.right.val)
            if sub_ans:
                ans.append(sub_ans)
        return ans
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([[3],[20,9],[15,7]],get_sol().zigzagLevelOrder(des([3,9,20,None,None,15,7])))
    def test02(self):
        self.assertEqual([[1]],get_sol().zigzagLevelOrder(des([1])))
    def test03(self):
        self.assertEqual([],get_sol().zigzagLevelOrder(des([])))
    def test04(self):
        self.assertEqual([[1],[3,2],[4,5]],get_sol().zigzagLevelOrder(des([1,2,3,4,None,None,5])))

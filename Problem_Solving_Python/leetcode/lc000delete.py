import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre_l, pre_r, post_l, post_r):
            if pre_l>pre_r: return None
            if pre_l==pre_r: return TreeNode(pre[pre_l])
            root = TreeNode(pre[pre_l])
            for new_post in range(post_l, post_r + 1):
                if post[new_post]==pre[pre_l + 1]:
                    break
            for new_pre in range(pre_l, pre_r + 1):
                if pre[new_pre]==post[post_r - 1]:
                    break
            root.left=helper(pre_l + 1, new_pre-1, post_l, new_post)
            root.right=helper(new_pre, pre_r, new_post + 1, post_r)
            return root

        n=len(pre)
        return helper(0,n-1,0,n-1)

def serialize(root):
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
    def test01(self):
        pre = [1,2,4,5,3,6,7]
        post = [4,5,2,6,7,3,1]
        Output= '1,2,3,4,5,6,7'
        actual_root = get_sol().constructFromPrePost(pre,post)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test02(self):
        pre = [2,4,5]
        post = [4,5,2]
        Output= '2,4,5'
        actual_root = get_sol().constructFromPrePost(pre,post)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test03(self):
        pre = [3,6,7]
        post = [6,7,3]
        Output= '3,6,7'
        actual_root = get_sol().constructFromPrePost(pre,post)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)

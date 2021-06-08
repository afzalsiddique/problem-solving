import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
###### UNIQUE BINARY TREE IS NOT POSSIBLE #####
###### ANY VALID BINARY TREE IS ACCEPTABLE #####
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # https://www.youtube.com/watch?v=LnHSOy7ctms
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        self.pre_idx=0
        def helper(post):
            if not post: return None
            root = TreeNode(pre[self.pre_idx])
            self.pre_idx+=1
            if len(post)==1: return root
            idx = post.index(pre[self.pre_idx]) # using dictionary will reduce time complexity

            left = post[:idx+1]
            right = post[idx+1:-1]

            root.left = helper(left)
            root.right = helper(right)
            return root

        return helper(post)

class Solution2:
    def constructFromPrePost(self, pre, post):
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(post) == 1: return root
            idx = pre.index(post[-2]) # using dictionary will reduce time complexity
            root.left = helper(pre[1: idx], post[:(idx - 1)])
            root.right = helper(pre[idx: ], post[(idx - 1):-1])
            return root

        return helper(pre,post)

class Solution3:
    def constructFromPrePost(self, pre, post):
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(pre) == 1: return root
            idx = post.index(pre[1]) # using dictionary will reduce time complexity
            root.left = helper(pre[1: idx+2], post[:idx+1])
            root.right = helper(pre[idx+2:], post[idx+1:-1])
            return root

        return helper(pre,post)

class Solution4:
    # wrong
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(pre)==1: return root
            post_idx = post.index(pre[1])
            pre_idx = pre.index(post[-2])
            left_pre = pre[1:pre_idx]
            right_pre = pre[pre_idx:]
            left_post = post[:post_idx+1]
            right_post = post[post_idx+1:-1]

            root.left = helper(left_pre, left_post)
            root.right = helper(right_pre,right_post)
            return root

        return helper(pre,post)

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
    def test04(self):
        pre = [2,1,3]
        post = [3,1,2]
        Output= 'many possible answers'
        actual_root = get_sol().constructFromPrePost(pre,post)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)


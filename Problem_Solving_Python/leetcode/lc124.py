# https://www.youtube.com/watch?v=6cA_NDtpyz8
import unittest
from collections import deque
from heapq import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxx=[float('-inf')]
        def max_sum_at_any_depth(root):
            if not root: return 0
            left=max_sum_at_any_depth(root.capacity)
            right=max_sum_at_any_depth(root.right)
            maxx[0]=max(maxx[0],left+right+root.val, left+root.val, right+root.val, root.val)
            return max(left+root.val,right+root.val, root.val)
        max_sum_at_any_depth(root)
        return maxx[0]
class Solution3:
    def __init__(self):
        self.maxx = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def postorder(root:TreeNode): # post order traversal
            if not root:return 0
            take_left=postorder(root.left)
            do_not_take_left=0
            left = max(take_left,do_not_take_left)
            take_right=postorder(root.right)
            do_not_take_right = 0
            right = max(take_right,do_not_take_right)
            self.maxx = max(self.maxx, left + right + root.val)
            return root.val + max(left, right)

        postorder(root)
        return self.maxx

class Solution2:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxx = float('-inf')
        def postorder(root:TreeNode):
            if not root:return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.maxx = max(self.maxx, left+right+root.val)
            return max (max(left,right)+root.val, 0)

        postorder(root)
        return self.maxx

def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<=1:return None
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



class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(48,Solution().maxPathSum(deserialize('5,4,8,11,null,13,4,7,2,null,null,null,1')))
    def test2(self):
        self.assertEqual(-1,Solution().maxPathSum(deserialize('-1,-2,-3')))
    def test3(self):
        self.assertEqual(6,Solution().maxPathSum(deserialize('1,2,3')))
    def test4(self):
        self.assertEqual(42,Solution().maxPathSum(deserialize('-10,9,20,null,null,15,7')))

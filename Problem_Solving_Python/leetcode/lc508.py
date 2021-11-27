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
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        di=defaultdict(int)
        def helper(root:TreeNode):
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            total = left+right+root.val
            di[total]+=1
            return total

        helper(root)

        # res = []
        # maxx=max(di.values())
        # for x in di:
        #     if di[x]==maxx:
        #         res.append(x)
        # return res

        # concise
        maxx = max(di.values())
        res = [x for x in di if di[x]==maxx]
        return res

def deserialize(data):
    sep,en = ',','#'
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


class tester(unittest.TestCase):
    def test1(self):
        root = deserialize('5,2,-3')
        Output= [2,-3,4]
        self.assertEqual(Output,Solution().findFrequentTreeSum(root))
    def test2(self):
        root = deserialize('5,2,-5')
        Output= [2]
        self.assertEqual(Output,Solution().findFrequentTreeSum(root))

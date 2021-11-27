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
# Wrong
class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        multiplier={}
        def get_multiplier(cnt:int)->int:
            if cnt==1: return 10
            if cnt in multiplier: return multiplier[cnt]
            ans= 10*get_multiplier(cnt-1)
            multiplier[cnt]=ans
            return ans
        def len_of_int(a:int)->int:
            if a==0: return 1
            cnt=0
            while a:
                a=a//10
                cnt+=1
            return cnt
        def helper(root:TreeNode):
            if not root: return []
            ret,ans = [],[]
            ans.extend(helper(root.left))
            ans.extend(helper(root.right))
            for sub_ans in ans:
                int_sub_ans = int(sub_ans)
                multi=get_multiplier(len_of_int(int_sub_ans))
                ret.append(str(root.val*multi+int_sub_ans))
            return ret if ret else [str(root.val)]


        ans = helper(root)
        print(ans)
        ans=list(map(int,ans))
        return sum(ans)

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

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(186,Solution().sumNumbers(deserialize('9,5,1')))
    def test2(self):
        self.assertEqual(1026,Solution().sumNumbers(deserialize('4,9,0,5,1')))
    def test3(self):
        self.assertEqual(5483,Solution().sumNumbers(deserialize('4,9,0,5,1,null,null,2')))
    def test4(self):
        self.assertEqual(25,Solution().sumNumbers(deserialize('1,2,3')))
    def test5(self):
        self.assertEqual(6363,Solution().sumNumbers(deserialize('5,3,2,7,0,6,null,null,null,0')))
    def test6(self):
        self.assertEqual(6377,Solution().sumNumbers(deserialize('5,3,2,7,1,6,null,null,null,4')))
    def test7(self):
        self.assertEqual(300,Solution().sumNumbers(deserialize('3,null,0,0')))
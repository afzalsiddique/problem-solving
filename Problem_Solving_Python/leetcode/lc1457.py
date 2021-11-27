import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/648534/JavaC%2B%2BPython-At-most-one-odd-occurrence
    # TOGGLE
    # Whenever meeting an element, toggle it in the set:
    # If set contains it, remove it. If set doesn't contain it, add it.
    cnt=0
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        sett=set()
        def toggle(val):
            if val not in sett: sett.add(val)
            else: sett.remove(val)

        def helper(root):
            if not root: return

            # compare with adding element to the path
            toggle(root.val)

            if not root.left and not root.right:
                self.cnt+=1 if len(sett)<=1 else 0
                # print(path)
            helper(root.left)
            helper(root.right)

            # compare with removing element from the path
            toggle(root.val)

        helper(root)
        return self.cnt

# Solution2
class MyCounter:
    def __init__(self):
        self.counter = Counter()
        self.digits_with_odd_freq=0
    def __auto_update(self, val):
        if self.counter[val]%2: self.digits_with_odd_freq+=1
        else: self.digits_with_odd_freq-=1
    def insert(self,val):
        self.counter[val]+=1
        self.__auto_update(val)
    def remove(self,val):
        self.counter[val]-=1
        self.__auto_update(val)
    def if_pseudo_palindrome(self): return not self.digits_with_odd_freq>1
class Solution2:
    cnt=0
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        path = []
        counter = MyCounter()
        def helper(root):
            if not root: return
            path.append(root.val)
            counter.insert(root.val)

            if not root.left and not root.right:
                # print(path)
                if counter.if_pseudo_palindrome(): self.cnt+=1
            helper(root.left)
            helper(root.right)

            counter.remove(root.val)
            path.pop()

        helper(root)
        return self.cnt

def deserialize(data):
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

class tester(unittest.TestCase):
    def test01(self):
        root = "2,3,1,3,1,null,1"
        root = deserialize(root)
        Output= 2
        self.assertEqual(Output,get_sol().pseudoPalindromicPaths(root))
    def test02(self):
        root = "2,1,1,1,3,null,null,null,null,null,1"
        root = deserialize(root)
        Output= 1
        self.assertEqual(Output,get_sol().pseudoPalindromicPaths(root))
    def test03(self):
        root = "9"
        root = deserialize(root)
        Output= 1
        self.assertEqual(Output,get_sol().pseudoPalindromicPaths(root))
    # def test04(self):
    # def test05(self):

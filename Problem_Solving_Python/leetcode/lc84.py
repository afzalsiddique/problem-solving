from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=vcv3REtIvEo&t=1020s
class Solution:
    def getJustBeforeNextSmaller(self, A, default, cnt=1):
        n=len(A)
        nextSmaller= [default] * n
        st=[]
        for i in range(n):
            while st and A[st[-1]]> A[i]: # nextSmaller, so it is going to be increasing stack. A[st[-1]]>A[i] -> take out while the top element is greater
                nextSmaller[st.pop()]=i-cnt
            st.append(i)
        return nextSmaller
    def getJustAfterPrevSmaller(self, A): # get indices which is right before the next smaller element
        n=len(A)
        tmp= self.getJustBeforeNextSmaller(A[::-1], 0, -1)
        nextSmaller=[(0 if x==0 else n-x+1) for x in tmp]
        return nextSmaller[::-1]
    def largestRectangleArea(self, A: List[int]) -> int:
        n=len(A)
        nextSmaller= self.getJustBeforeNextSmaller(A, n - 1)
        prevSmaller=self.getJustAfterPrevSmaller(A)
        res=float('-inf')
        for i in range(n):
            width=nextSmaller[i]-prevSmaller[i]+1
            res=max(res,width*A[i])
        return res
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, n,mx_area= [], len(heights),0
        left,right=[0 for _ in range(n)],[0 for _ in range(n)]

        for i in range(n):
            if not stack:
                left[i]=0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]: # it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                left[i]=stack[-1]+1 if stack else 0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
        print(left)
        stack = []
        for i in reversed(range(n)):
            if not stack:
                right[i]=n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:# it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                right[i]=stack[-1]-1 if stack else n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
        print(right)
        for i,h in enumerate(heights):
            mx_area = max(mx_area,(right[i]-left[i]+1)*h)
        return mx_area


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(10, get_sol().largestRectangleArea([2,1,5,6,2,3]))
    def test02(self):
        self.assertEqual(4, get_sol().largestRectangleArea([2,4]))
    def test03(self):
        self.assertEqual(2, get_sol().largestRectangleArea([1,1]))
    def test04(self):
        self.assertEqual(15, get_sol().largestRectangleArea([1,5,5,5,1]))
    def test05(self):
        self.assertEqual(20, get_sol().largestRectangleArea([3,6,5,7,4,8,1,0]))

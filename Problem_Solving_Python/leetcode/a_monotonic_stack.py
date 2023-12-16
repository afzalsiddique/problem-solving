from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt;
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    INVALID=-1
    # if we want immediate index before next smaller cnt will be -1
    # default: if there is no next smaller then default will be returned
    def getJustBeforeNextSmaller(self, A, op, default, cnt=-1):
        # get indices which is right before the next smaller element
        # index:    0   1   2   3   4
        # items:    5   6   5   8   1
        #           3   .   .   .   .
        # next smaller of 5 is 1 which is in index 4. So right before index 4 is index 3
        n=len(A)
        nextSmaller=[self.INVALID]*n
        # nextSmaller=[initial]*n # if this line is used then -> "while st: nextSmaller[st.pop()]=initial" is not required
        st=[]
        for i in range(n):
            while st and op(A[st[-1]], A[i]): # nextSmaller, so it is going to be increasing stack. A[st[-1]]>A[i] -> take out while the top element is greater
                nextSmaller[st.pop()]=i+cnt
            st.append(i)
        while st:
            nextSmaller[st.pop()]=default
        return nextSmaller
    def getJustAfterPrevSmaller(self, A): # get indices which is right before the next smaller element
        n=len(A)
        B=A[::-1]
        tmp=self.getJustBeforeNextSmaller(B,gt,0,1)
        nextSmaller=[]
        for x in tmp:
            if x!=0:
                nextSmaller.append(n-x+1)
            else:
                nextSmaller.append(0)
        return nextSmaller[::-1]
    def getNextSmaller(self,A):
        n=len(A)
        nextSmaller=[-1]*n
        st=[]
        for i in range(n):
            while st and A[st[-1]]>A[i]:
                idx=st.pop()
                nextSmaller[idx]=i
            st.append(i)
        return nextSmaller
    def getPrevSmaller(self,A):
        n=len(A)
        prevSmaller=[-1]*n
        st=[]
        for i in range(n-1,-1,-1): # one change here
            while st and A[st[-1]]>A[i]:
                idx=st.pop()
                prevSmaller[idx]=i
            st.append(i)
        return prevSmaller


class Tester(unittest.TestCase):
    def test01(self):
        A=[1, 2, 3, 2]
        self.assertEqual([3, 3, 2, 3], get_sol().getJustBeforeNextSmaller(A, gt,len(A)-1))
    def test02(self):
        A=[2, 3, 3, 1, 2]
        self.assertEqual([2, 2, 2, 4, 4], get_sol().getJustBeforeNextSmaller(A, gt,len(A)-1))
    def test03(self):
        A=[3, 1, 5, 6, 4, 2]
        self.assertEqual([0, 5, 3, 3, 4, 5], get_sol().getJustBeforeNextSmaller(A, gt,len(A)-1))
    def test04(self):
        A=[3, 3, 2, 2, 3, 1, 1, 4, 1, 3]
        self.assertEqual([1, 1, 4, 4, 4, 9, 9, 7, 9, 9], get_sol().getJustBeforeNextSmaller(A, gt,len(A)-1))
    def test05(self):
        A=[3, 3]
        self.assertEqual([1, 1], get_sol().getJustBeforeNextSmaller(A, gt,len(A)-1))
    def test06(self):
        A=[1, 2, 3, 2]
        self.assertEqual([0, 1, 2, 1], get_sol().getJustAfterPrevSmaller(A))
    def test07(self):
        A=[2, 3, 3, 1, 2]
        self.assertEqual([0, 1, 1, 0, 4], get_sol().getJustAfterPrevSmaller(A))
    def test08(self):
        A=[3, 1, 5, 6, 4, 2]
        self.assertEqual([0, 0, 2, 3, 2, 2], get_sol().getJustAfterPrevSmaller(A))
    def test09(self):
        A=[3, 3, 2, 2, 3, 1, 1, 4, 1, 3]
        self.assertEqual([0, 0, 0, 0, 4, 0, 0, 7, 0, 9], get_sol().getJustAfterPrevSmaller(A))
    def test10(self):
        A=[3, 3]
        self.assertEqual( [0, 0], get_sol().getJustAfterPrevSmaller(A))
    def test11(self):
        self.assertEqual( [3,3,3,-1,-1], get_sol().getNextSmaller([1,2,3,0,1]))

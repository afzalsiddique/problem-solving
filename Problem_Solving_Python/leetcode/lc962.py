import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC%2B%2BPython-O(N)-Using-Stack
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC++Python-O(N)-Using-Stack/211767
    # time O(n) space O(n)
    def maxWidthRamp(self, A):
        n=len(A)
        maxx=0
        st=[] # decreasing stack
        for i in range(n):
            if not st or A[st[-1]]>A[i]:
                st.append(i)
        for i in range(n-1,-1,-1):
            while st and A[st[-1]]<=A[i]:
                maxx=max(maxx,i-st.pop())
        return maxx
class Solution2:
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC%2B%2BPython-O(N)-Using-Stack
    # time O(nlogn) space O(n)
    def maxWidthRamp(self, A):
        n=len(A)
        st=[] # increasing stack
        indices =[] # corresponding indices of the stack
        maxx=0
        for i in range(n-1,-1,-1):
            if not st or st[-1]<A[i]:
                st.append(A[i])
                indices.append(i)
            else:
                fake_idx = bisect_left(st,A[i])
                real_idx = indices[fake_idx]
                maxx=max(maxx,real_idx-i)
        return maxx
class tester(unittest.TestCase):
    def test_1(self):
        nums = [6,0,8,2,1,5]
        Output= 4
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))
    def test_2(self):
        nums = [9,8,1,0,1,9,4,0,4,1]
        Output= 7
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))
    def test_3(self):
        nums = [1,0,0,1]
        Output= 3
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/longest-well-performing-interval/discuss/335163/O(N)-Without-Hashmap.-Generalized-ProblemandSolution%3A-Find-Longest-Subarray-With-Sum-greater-K.
    # https://leetcode.com/problems/maximum-width-ramp/
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC++Python-O(N)-Using-Stack/211767
    def longestWPI(self, hours: List[int]) -> int:
        prefix=[0]
        for i in range(len(hours)):
            prefix.append(prefix[-1]+1) if hours[i]>8 else prefix.append(prefix[-1]-1)
        # we don't need hours anymore and will only work with prefix
        n=len(prefix)
        st=[] # decreasing stack
        for i in range(n):
            if not st or prefix[i]<prefix[st[-1]]:
                st.append(i)

        maxx=0
        for j in range(n-1,-1,-1):
            while st and prefix[j]>prefix[st[-1]]:
                i=st.pop()
                maxx=max(maxx,j-i)
        return maxx


class Tester(unittest.TestCase):
    def test_1(self):
        hours = [9,9,6,0,6,6,9]
        Output= 3
        self.assertEqual(Output,get_sol().longestWPI(hours))
    # def test_2(self):
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
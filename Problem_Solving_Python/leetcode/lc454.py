from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        di=defaultdict(int)
        for a in A:
            for b in B:
                di[a+b]+=1
        count=0
        for c in C:
            for d in D:
                if -c-d in di:
                    count+=di[-c-d]
        return count
class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.fourSumCount(A = [ 1, 2],
                                  B = [-2,-1],
                                  C = [-1, 2],
                                  D = [ 0, 2])
        expected = 2
        self.assertEqual(expected, actual)

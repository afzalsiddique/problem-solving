import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-latest-group-of-size-m/discuss/806786/JavaC%2B%2BPython-Count-the-Length-of-Groups-O(N)
    def findLatestStep(self, A: List[int], m: int) -> int:
        res = -1; n = len(A)
        length=[0]*(n+2)
        count = defaultdict(int)
        for i in range(n):
            a=A[i]
            left=length[a-1]
            right=length[a+1]
            tmp = left+right+1
            length[a - left] = tmp
            length[a + right] = tmp
            count[left]-=1
            count[right]-=1
            count[tmp]+=1
            if count[m] > 0:
                res = i + 1
        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr,m = [3,5,1,2,4],1
        Output= 4
        self.assertEqual(Output, get_sol().findLatestStep(arr,m))
    def test_2(self):
        arr,m = [3,1,5,4,2],2
        Output= -1
        self.assertEqual(Output, get_sol().findLatestStep(arr,m))
    def test_3(self):
        arr,m = [1],1
        Output= 1
        self.assertEqual(Output, get_sol().findLatestStep(arr,m))
    def test_4(self):
        arr,m = [2,1],2
        Output= 2
        self.assertEqual(Output, get_sol().findLatestStep(arr,m))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
